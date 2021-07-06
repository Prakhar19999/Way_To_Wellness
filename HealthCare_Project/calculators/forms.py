from django import forms
from .models import *

class UserDetailForm(forms.ModelForm):
    class Meta:
        model=UserDetail
        fields=['name','email_id','mobile_no']

class BMIform(forms.ModelForm):
    class Meta:
        model=BMI
        fields=['weight','height_ft','height_inches']

class WaterForm(forms.ModelForm):
    class Meta:
        model=Water
        fields=['weight','exercise_time']

class WHRform(forms.ModelForm):
    class Meta:
        model=WHR
        fields=['waist','hip']

class BMRform(forms.ModelForm):
    class Meta:
        model=BMR
        fields=['weight','height_ft','height_inches','age','gender']

class NutriForm(forms.ModelForm):
    class Meta:
        model=CalMacroNutri
        fields=['weight','height_ft','height_inches','age','gender','lifestyle']

class BFform(forms.ModelForm):
    class Meta:
        model=BF
        fields=['weight','waist','wrist','hip','forearm','gender']