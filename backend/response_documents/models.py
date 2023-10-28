from django.db import models
from templates.models import Templates

# Create your models here.

class ResponseDocument(models.Model):
    template_id = models.ForeignKey(Templates, on_delete=models.CASCADE)
    response_document = models.FileField(upload_to="correspondence/", blank=True, null=True)

    def __str__(self) -> str:
        return self.id