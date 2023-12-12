from django.db import models
class Staff(models.Model):
    staff_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name