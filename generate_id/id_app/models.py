# Create your models here.

from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=200)
    aadhar_card = models.CharField(max_length=12, unique=True)
    driver_license_no = models.CharField(max_length=20, unique=True)
    transporter_name = models.CharField(max_length=200,blank=True,null=True)
    training_date = models.DateField(blank=True,null=True)
    expiry_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name

