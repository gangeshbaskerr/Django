from django import forms
from .models import BusDetails

# forms.py
class TicketForm(forms.Form):
    Bus_No = forms.CharField(max_length=20)
    Destination = forms.CharField(max_length=100)
    No_of_Persons = forms.IntegerField()
