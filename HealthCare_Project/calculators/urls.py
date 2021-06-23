from django.urls import path,include
from .views import *

urlpatterns = [
    path('',calculators,name="calculators"),
    path('bmi/',BMI,name="BMI"),
    path('water/',Water,name="Water"),
    path('whr/',WHR,name="WHR"),
    path('bmr/',BMR,name="BMR"),
    path('nutri/',CalMacroNutri,name="nutri"),
    path('bf/',BF,name="BF"),
]