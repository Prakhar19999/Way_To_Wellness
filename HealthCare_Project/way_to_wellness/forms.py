from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['name','email','mobile_no','weight','height_ft','height_inches','age','date','time','msg']