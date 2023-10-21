from django.db import models
from django.utils import timezone
from datetime import timedelta, date, datetime

# Create your models here.

HOLIDAYS = [
    date(2023,1,1),
    date(2023,12,24),
    date(2023,12,25),
]

# Seems like this method should be a class method
def add_business_days(from_date, add_days):
    current_date = from_date.date()  # Extract the date from the datetime object
    iterations = 0
    while add_days > 0:
        if iterations > 15:  # Prevent more than 15 day's worth of iterations
            raise ValueError("Too many iterations in add_business_days")
        current_date += timedelta(days=1)
        if current_date.weekday() < 5 and current_date not in HOLIDAYS:  
            add_days -= 1
        iterations += 1
    return timezone.make_aware(datetime.combine(current_date, from_date.time()))

def get_default_due_date():
    return add_business_days(timezone.now(), 10)


class ActionRequest(models.Model):
    action_request_title = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=50)
    due_date = models.DateTimeField(default=get_default_due_date)
    comments = models.TextField(blank=True, default="")
    documents = models.FileField(upload_to="arts-documents/", blank=True, null=True)

    def __str__(self):
        return ', '.join(f"{key}: {value}" for key, value in vars(self).items())
