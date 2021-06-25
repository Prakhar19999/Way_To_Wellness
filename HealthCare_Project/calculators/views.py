from django.shortcuts import render
from .models import *
from .forms import *
from json import dumps
from way_to_wellness.forms import *

def calculators(requests):
    calculators=Calculator.objects.all()
    ap_form=AppointmentForm()
    count=0
    count=Calculator.objects.all().count()
    context={'calculator':calculators,'count':count,'ap_form':ap_form}
    return render(requests,'calculators/calculator_base.html',context)

def BMI(requests):
    bmiform=BMIform()
    bmi=0
    if requests.method=='POST':
        bmiform=BMIform(requests.POST)
        if(bmiform.is_valid()):
            bmiform.save()
            numerator=float(requests.POST.get('weight'))
            denominator=float(requests.POST.get('height'))*float(requests.POST.get('height'))
            bmi=numerator/denominator
    bmiJSON=dumps({
        'bmi':bmi
    },default=str)
    context={'bmi_result':bmiJSON,'bmi':bmi}
    return render(requests,'calculators/BMI.html',context)

def Water(requests):
    water_form=WaterForm()
    ans=0
    if requests.method =='POST':
        water_form=WaterForm(requests.POST)
        if water_form.is_valid():
            water_form.save()
            weight=float(requests.POST.get('weight'))
            time=float(requests.POST.get('exercise_time'))
            F1=weight*0.044
            F2=(time/30)*0.355
            ans=F1+F2
    waterJSON=dumps({
        'water':ans
    },default=str)
    context={'water_result':waterJSON,'water':ans}
    return render(requests,'calculators/water.html',context)

def WHR(requests):
    whr_form=WHRform()
    whr=0
    if requests.method=='POST':
        whr_form=WHRform(requests.POST)
        if whr_form.is_valid():
            whr_form.save()
            num=float(requests.POST.get('waist'))
            den=float(requests.POST.get('hip'))
            whr=num/den
    whrJSON=dumps({
        'whr':whr
    })
    context={'whr_result':whrJSON,'whr':whr}
    return render(requests,'calculators/WHR.html',context)

def BMR(requests):
    bmr_form=BMRform()
    bmr=0
    if requests.method=='POST':
        bmr_form=BMRform(requests.POST)
        if bmr_form.is_valid():
            bmr_form.save()
            weight=float(requests.POST.get('weight'))
            height=float(requests.POST.get('height'))*2.5
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            if gender=="Male":
                bmr=655+(9.6*weight)+(1.8*height)-(4.7*age)
            else:
                bmr=66+(13.7*weight)+(5*height)-(6.8*age)
    bmrJSON=dumps({
        'bmr':bmr
    },default=str)
    context={'bmr_result':bmrJSON,'bmr':bmr}
    return render(requests,'calculators/BMR.html',context)

def CalMacroNutri(requests):
    nutri_form=NutriForm()
    bmr_men=0
    bmr_women=0
    bmr=0
    if requests.method=='POST':
        nutri_form=NutriForm(requests.POST)
        if nutri_form.is_valid():
            nutri_form.save()
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
    bf_form=BFform()
    body_fat_weight=0
    body_fat_percentage=0
    if requests.method=='POST':
        bf_form=BFform(requests.POST)
        if bf_form.is_valid():
            bf_form.save()
            gender=requests.POST.get('gender')
            weight=float(requests.POST.get('weight'))
            if gender=="Female":
                f1=float(requests.POST.get('weight'))*0.732+8.987
                f2=float(requests.POST.get('wrist'))/3.140
                f3=float(requests.POST.get('waist'))*0.157
                f4=float(requests.POST.get('hip'))*0.249
                f5=float(requests.POST.get('forearm'))*0.434
                lean_body_mass=f1+f2+f5-f2-f3
                body_fat_weight=weight-lean_body_mass
                body_fat_percentage=(body_fat_weight*100)/weight
            elif gender=="Male":
                f1=float(requests.POST.get('weight'))*1.082+94.42
                f2=float(requests.POST.get('waist'))*4.15
                lean_body_mass=f1-f2
                body_fat_weight=weight-lean_body_mass
                body_fat_percentage=(body_fat_weight*100)/weight
    bfJSON=dumps({
        'bfw':body_fat_weight,
        'bfp':body_fat_percentage,
    },default=str)
    context={'bf_result':bfJSON,'bfw':body_fat_weight,'bfp':body_fat_percentage}
    return render(requests,'calculators/BF.html',context)