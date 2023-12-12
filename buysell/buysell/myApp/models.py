# vehicles/models.py
from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    type_of_vehicle = models.CharField(max_length=10)  # Car or Motorbike
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    year_of_purchase = models.IntegerField()
    kilometers = models.IntegerField()
    color = models.CharField(max_length=50)
    registered_state = models.CharField(max_length=2)
    number_of_owners = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    mode_of_payment = models.CharField(max_length=50)
