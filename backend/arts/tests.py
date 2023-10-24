from django.test import TestCase
from moto import mock_s3
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import ActionRequest, add_business_days
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import boto3


class ActionRequestModelTestCase(TestCase):

    def test_action_request_creation(self):
        action_request = ActionRequest.objects.create(
            action_request_title="Test Title",
            action="Sample"
        )
        self.assertIsNotNone(action_request.id)
        self.assertEqual(action_request.action_request_title, "Test Title")
        self.assertEqual(action_request.action, "Sample")

        # Ensure the created_on is almost equal to timezone.now()
        self.assertAlmostEqual(
            action_request.created_on, timezone.now(),
            delta=timedelta(seconds=5)
        )

        # Compute expected due date which is 10 business days from now
        expected_due_date = add_business_days(timezone.now(), 10)

        # Ensure the due_date is almost equal to expected_due_date
        self.assertAlmostEqual(
            action_request.due_date, expected_due_date,
            delta=timedelta(seconds=5)
        )



class ActionRequestModelFieldValidationTestCase(TestCase):

    def test_action_request_title_length(self):
        # Generate a title that exceeds 255 characters
        long_title = 'A' * 256
        with self.assertRaises(ValidationError):
            action_request = ActionRequest(action_request_title=long_title, action='TestAct')
            action_request.full_clean()

    def test_action_length(self):
        # Generate an action that exceeds 10 characters
        long_action = 'A' * 256
        with self.assertRaises(ValidationError):
            action_request = ActionRequest(action_request_title='Test Title', action=long_action)
            action_request.full_clean()

    def test_action_request_title_not_null(self):
        with self.assertRaises(IntegrityError):
            # This will try to set action_request_title to None, which should be disallowed
            action_request = ActionRequest.objects.create(action_request_title=None, action='TestAct')

    def test_action_not_null(self):
        with self.assertRaises(IntegrityError):
            # This will try to set action to None, which should be disallowed
            action_request = ActionRequest.objects.create(action_request_title='Test Title', action=None)

    def test_action_request_title_not_empty(self):
        with self.assertRaises(ValidationError):
            action_request = ActionRequest(action_request_title='', action='TestAct')
            action_request.full_clean()

    def test_action_not_empty(self):
        with self.assertRaises(ValidationError):
            action_request = ActionRequest(action_request_title='Test Title', action='')
            action_request.full_clean()


class ActionRequestModelS3FileFieldTestCase(TestCase):

    @mock_s3
    def test_documents_field_s3(self):
        # Create a mock S3 bucket
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        # Create a simple in-memory text file for testing
        test_file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")

        action_request = ActionRequest.objects.create(
            action_request_title='Test Title',
            action='TestAct',
            documents=test_file
        )

        self.assertIn('test_', action_request.documents.name)


class ActionRequestModelFileFieldUpdateTestCase(TestCase):

    def test_documents_field_update(self):
        # Create a simple in-memory text file for testing
        test_file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")

        action_request = ActionRequest.objects.create(
            action_request_title='Test Title',
            action='TestAct',
            documents=test_file
        )

        # Check that the document was saved correctly
        self.assertIn('test_', action_request.documents.name)

        # Remove the document
        action_request.documents.delete()
        action_request.save()

        # Reload the instance from the database to check the updated state
        action_request.refresh_from_db()

        # Check that 'documents' is None
        self.assertTrue(not action_request.documents.name)



class ActionRequestModelFileFieldTestCase(TestCase):

    def test_adding_document_later(self):
        # Create an ActionRequest instance without specifying a 'documents' value
        action_request = ActionRequest.objects.create(
            action_request_title='Test Title',
            action='TestAct'
        )

        # Check that the instance was created successfully and that 'documents' is None
        self.assertTrue(not action_request.documents.name)

        # Add a document to the existing ActionRequest
        test_file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")
        action_request.documents = test_file
        action_request.save()

        # Check that the document was saved correctly
        self.assertTrue(action_request.documents.name)  # Checks that a filename exists


class DueDateTestCase(TestCase):

    def test_skip_weekends(self):
        # Start on a Friday
        start_date = timezone.make_aware(datetime(2023, 1, 6, 12))  
        due_date = add_business_days(start_date, 10)
        
        # 10 business days from Friday, Jan 6, 2023 should be Friday, Jan 20, 2023
        self.assertEqual(due_date.date(), date(2023, 1, 20))
        
    def test_skip_holidays(self):
        # Assuming Jan 1 and Jan 2 are holidays
        start_date = timezone.make_aware(datetime(2023, 12, 30, 12))
        due_date = add_business_days(start_date, 10)
        
        # 10 business days from Saturday, Dec 30, 2022, considering 2 holidays, should be Jan 13, 2023
        self.assertEqual(due_date.date(), date(2024, 1, 13))
        
    def test_start_on_holiday(self):
        # Start on a holiday
        start_date = timezone.make_aware(datetime(2023, 1, 1, 12))
        due_date = add_business_days(start_date, 10)
        
        # 10 business days from Sunday (which is also a holiday), Jan 1, 2023 should be Jan 13, 2023
        self.assertEqual(due_date.date(), date(2023, 1, 13))
        
    def test_sequential_holidays(self):
        # If you have a scenario where there are several holidays in a row, you can test it here
        pass
        
    def test_holiday_on_monday(self):
        # Start on a holiday that's on a Monday
        start_date = timezone.make_aware(datetime(2023, 7, 3, 12))
        due_date = add_business_days(start_date, 10)
        
        # Calculate the expected due date by skipping the holiday and then counting 10 business days
        self.assertEqual(due_date.date(), date(2023, 7, 18))
        
    def test_holiday_on_friday(self):
        # Start on a holiday that's on a Friday
        pass
        
    def test_default_due_date_on_creation(self):
        # Create an ActionRequest without specifying a due_date
        ar = ActionRequest.objects.create(action_request_title='Test', action='TestAct')
        
        # Now, compare ar.due_date with the expected date based on when it was created
        expected_due_date = add_business_days(timezone.now(), 10)
        self.assertEqual(ar.due_date.date(), expected_due_date.date())
