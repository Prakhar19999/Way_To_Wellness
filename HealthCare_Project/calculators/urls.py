from django.urls import path,include
from .views import *

urlpatterns = [
    path('',calculators,name="calculators"),
    path('bmi/',BodyMassIndex,name="BMI"),
    path('water/',WaterCalculator,name="Water"),
    path('whr/',WaistToHip,name="WHR"),
    path('bmr/',BasalMetabolicRate,name="BMR"),
    path('nutri/',Calorie,name="nutri"),
    path('bf/',BodyFat,name="BF"),
]