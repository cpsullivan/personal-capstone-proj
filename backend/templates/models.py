from django.db import models

# Create your models here.

class Templates(models.Model):
    template_type = models.CharField(max_length=50)
    template_use = models.CharField(max_length=255) #Use this field to describe how to use the template
    template_document = models.FileField(upload_to="templates/",blank=True,null=True)

    def __str__(self) -> str:
        return self.id