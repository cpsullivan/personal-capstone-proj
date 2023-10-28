from django.db import models

# Create your models here.

class OrganizationElement(models.Model):
    org_element_name = models.CharField(50)

    def __str__(self) -> str:
        return self.id