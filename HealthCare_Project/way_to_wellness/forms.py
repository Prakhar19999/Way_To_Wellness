from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type= 'date'

class TimeInput(forms.TimeInput):
    input_type= 'time'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        widgets={'date':DateInput(),'time':TimeInput()}
        fields=['name','email','mobile_no','weight','height','age','date','time','msg']