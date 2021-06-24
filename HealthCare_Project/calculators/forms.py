from django import forms
from .models import *

class BMIform(forms.ModelForm):
    class Meta:
        model=BMI
        fields=['weight','height']

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
        fields=['weight','height','age','gender']

class NutriForm(forms.ModelForm):
    class Meta:
        model=CalMacroNutri
        fields=['weight','height','age','gender','lifestyle']

class BFform(forms.ModelForm):
    class Meta:
        model=BF
        fields=['weight','waist','wrist','forearm']