from django.db import models
from correspondent_address import CorrespondentAddress

# Create your models here.

class Correspondent(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address_id = models.ForeignKey(CorrespondentAddress, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id