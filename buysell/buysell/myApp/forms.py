# vehicles/forms.py
from django import forms
from .models import Vehicle

class SellForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields='__all__'
        #exclude = ['type_of_vehicle']

class BuyForm(forms.Form):
    type_of_vehicle = forms.ChoiceField(choices=[('Car', 'Car'), ('Motorbike', 'Motorbike')])
    brand = forms.CharField(max_length=50)
    kilometers = forms.IntegerField()
    number_of_owners = forms.IntegerField(required=False)
    expected_price_range = forms.IntegerField()

