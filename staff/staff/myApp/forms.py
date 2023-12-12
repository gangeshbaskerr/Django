# staff/forms.py
from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'name', 'age', 'mobile_no', 'email_id', 'department']
