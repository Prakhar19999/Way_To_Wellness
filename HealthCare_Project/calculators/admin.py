from django.contrib import admin
from .models import *


calculators=[BMI,BMR,BF,Water,WHR,CalMacroNutri,Calculator]
admin.site.register(calculators)