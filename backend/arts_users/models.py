from django.db import models
from organization_element.models import OrganizationElement

# Create your models here.

USER_TYPES = [
    ("USR", "User"),
    ("SPU", "Super User")
]

class ArtsUser(models.Model):
    user_last_name = models.CharField(max_length=50)
    user_first_name = models.CharField(max_length=50)
    user_org_element = models.ForeignKey(OrganizationElement, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=3, choices=USER_TYPES, default="User")

    def __str__(self) -> str:
        return self.id