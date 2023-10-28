from django.db import models

# Create your models here.

class CorrespondentAddress(models.Model):
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=12)

    def __str__(self):
        return self.id

#Look at APIs from which the model can fetch data for the Country and City fields. GeoNames.org is a possible data source.

#Look at including a validator for the PostalCode field. The validator would need to be configured based on the country selected in the Country field.