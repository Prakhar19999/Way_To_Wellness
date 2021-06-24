from django.shortcuts import render
from .models import *
from .forms import *

def calculators(requests):
    bmiform=BMIform()
    context={'bmiform':bmiform}
    return render(requests,'calculators/calculator_base.html',context)

def BMI(requests):
    bmiform=BMIform()
    bmi=0
    if requests.method=='POST':
        bmiform=BMIform(requests.POST)
        if(bmiform.is_valid()):
            numerator=float(requests.POST.get('weight'))
            denominator=float(requests.POST.get('height'))*float(requests.POST.get('height'))
            bmi=numerator/denominator
    return render(requests,'calculators/BMI.html')

def Water(requests):
    form=WaterForm()
    ans=0
    if requests.method =='POST':
        form=WaterForm(requests.POST)
        if form.is_valid():
            weight=float(requests.POST.get('weight'))
            time=float(requests.POST.get('exercise_time'))
            F1=weight*0.044
            F2=(time/30)*0.355
            ans=F1+F2
    context={'water_form':form}
    return render(requests,'calculators/water.html',context)

def WHR(requests):
    form=WHRform()
    whr=0
    if requests.method=='POST':
        form=WHRform(requests.POST)
        if form.is_valid():
            num=float(requests.POST.get('waist'))
            den=float(requests.POST.get('hip'))
            whr=num/den
    return render(requests,'calculators/WHR.html')

def BMR(requests):
    form=BMRform()
    bmr_men=0
    bmr_women=0
    if requests.method=='POST':
        form=BMRform(requests.POST)
        if form.is_valid():
            weight=float(requests.POST.get('weight'))
            height=float(requests.POST.get('height'))*2.5
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            print(gender)
            if gender=="Male":
                bmr_men=655+(9.6*weight)+(1.8*height)-(4.7*age)
            else:
                bmr_women=66+(13.7*weight)+(5*height)-(6.8*age)
    print(bmr_men)
    print(bmr_women)
    return render(requests,'calculators/BMR.html')

def CalMacroNutri(requests):
    form=NutriForm()
    bmr_men=0
    bmr_women=0
    bmr=0
    if requests.method=='POST':
        form=NutriForm(requests.POST)
        if form.is_valid():
            weight=float(requests.POST.get('weight'))
            height=float(requests.POST.get('height'))*2.5
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            lifestyle=requests.POST.get('lifestyle')
            if gender=="Male":
                bmr_men=1
                bmr=655+(9.6*weight)+(1.8*height)-(4.7*age)
            else:
                bmr_women=1
                bmr=66+(13.7*weight)+(5*height)-(6.8*age)
            if lifestyle=="Sedentary":
                bmr=bmr*1.2
            elif lifestyle=="Lightly Active":
                bmr=bmr*1.375
            elif lifestyle=="Moderately Active":
                bmr=bmr*1.55
            elif lifestyle=="Very Active":
                bmr=bmr*1.725
            elif lifestyle=="Extra Active":
                bmr=bmr*1.9
    return render(requests,'calculators/nutri.html')

def BF(requests):
    form=BFform()
    male=0
    female=0
    bf=0
    if requests.method=='POST':
        form=BFform(requests.POST)
        if form.is_valid():
            gender=requests.POST.get('gender')
            weight=float(requests.POST.get('weight'))
            if gender=="Male":
                male=1
                f1=float(requests.POST.get('weight'))*0.732+8.987
                f2=float(requests.POST.get('wrist'))/3.140
                f3=float(requests.POST.get('waist'))*0.157
                f4=float(requests.POST.get('hip'))*0.249
                f5=float(requests.POST.get('forearm'))*0.434
                lean_body_mass=f1+f2+f5-f2-f3
                body_fat_weight=weight-lean_body_mass
                body_fat_percentage=(body_fat_weight*100)/weight
            elif gender=="Female":
                female=1
                f1=float(requests.POST.get('weight'))*1.082+94.42
                f2=float(requests.POST.get('waist'))*4.15
                lean_body_mass=f1-f2
                body_fat_weight=weight-lean_body_mass
                body_fat_percentage=(body_fat_weight*100)/weight
            else:
                print("Select gender")
    return render(requests,'calculators/BF.html')