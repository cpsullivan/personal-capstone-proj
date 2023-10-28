from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date
from correspondent import correspondent
from response_documents.models import ResponseDocument

# Create your models here.

HOLIDAYS = [
    '2023-12-24',
    '2023-12-25',
    '2023-12-26',
    '2024-1-1'
]

def add_business_days(from_date, add_days):
    current_date = from_date.date()  # Extract the date from the datetime object
    iterations = 0
    while add_days > 0:
        if iterations > 15:  # Prevent more than a 15 day's worth of iterations
            raise ValueError("Too many iterations in add_business_days")
        current_date += timedelta(days=1)
        if current_date.weekday() < 5 and current_date not in HOLIDAYS:  
            add_days -= 1
        iterations += 1
    return timezone.make_aware(datetime.combine(current_date, from_date.time()))  


class ActionRequest(models.Model):
    action_request_title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    correspondent_id = models.ForeignKey(correspondent, blank=True, on_delete=models.CASCADE) #maybe not CASCADE; what other options are there?
    action = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    comments = models.TextField(blank=True, default="")
    documents = models.ForeignKey(ResponseDocument, blank=True, null=True) #Verify if you can do 'blank=True' and 'null=True' for a ForiegnKey field; the user won't always upload a response document to the action request when creating it

    def save(self, *args, **kwargs):
        if not self.created_on:
            self.created_on = date.today()
        super(ActionRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.id