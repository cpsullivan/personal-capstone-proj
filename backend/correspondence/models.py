from django.db import models
from django.utils import timezone


class Correspondence(models.Model):
    CORRESPONDENCE_TYPES = [
        ('LTR', "Letter"),
        ('EML', "Email"),
        ('PHN', "Phonecall"),
        ('FAX', "Fax")
    ]

    correspondence_type = models.CharField(max_length=3, choices=CORRESPONDENCE_TYPES, default='Email')
    correspondence_date = models.DateTimeField()
    correspondence_document = models.FileField(upload_to="documents/", blank=True, null=True)

    def __str__(self):
        return self.id
