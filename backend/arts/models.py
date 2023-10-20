from django.db import models
from django.utils import timezone

# Create your models here.

class ActionRequest(models.Model):
    action_request_title = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=10)
    due_date = models.DateTimeField(default=timezone.now)
    documents = models.FileField(upload_to="documents/", blank=True, null=True)

    def __str__(self):
        return self.action_request_title