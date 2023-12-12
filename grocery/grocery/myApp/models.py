from django.db import models

class Grocery(models.Model):
    TYPE_CHOICES = [
        ('Oil', 'Oil'),
        ('Grains', 'Grains'),
        ('Cosmetics', 'Cosmetics'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    quantity = models.IntegerField()
    rate_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
