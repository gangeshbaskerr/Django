from django.db import models

class FoodItem(models.Model):
    FOOD_TYPES = [
        ('Vegetable', 'Vegetable'),
        ('Fruit', 'Fruit'),
        ('Nuts', 'Nuts'),
    ]

    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
    vitamin_present = models.CharField(max_length=50)

    def __str__(self):
        return self.name

