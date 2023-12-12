from django.db import models

class Income(models.Model):
    STATUS = [
        ('Professional', 'Professional'),
        ('Politician', 'Politician'),
        ('Employee', 'Employee'),
    ]

    name = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=8, decimal_places=0)
    totDepositValue = models.DecimalField(max_digits=8, decimal_places=3)
    totAssetValue = models.DecimalField(max_digits=8, decimal_places=3)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name

