from django.db import models

class BusDetails(models.Model):
    Bus_No = models.CharField(max_length=20)
    Departure_Time = models.DateTimeField()
    Destinations = models.CharField(max_length=200)
    Seats_Available = models.IntegerField()
    TicketCosts = models.CharField(max_length=200)

    def _str_(self):
        return self.Bus_No
