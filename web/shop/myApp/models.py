from django.db import models
# Create your models here.
class Details(models.Model):
 firstName=models.CharField(max_length=30)
 secondName = models.CharField(max_length=30)
 mobile=models.PositiveIntegerField()
