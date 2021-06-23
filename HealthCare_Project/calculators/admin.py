from django.contrib import admin
from .models import *


calculators=[BMI,BMR,BF,Water,WHR,CalMacroNutri]
admin.site.register(calculators)