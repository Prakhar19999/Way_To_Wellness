from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['name','email','mobile_no','weight','height','age','date','time','msg']