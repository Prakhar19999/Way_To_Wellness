from django.shortcuts import render
from .models import *
from .forms import *
from json import dumps
from way_to_wellness.forms import *

def calculators(requests):
    return render(requests,'calculators/calculator_base.html')

def BMI(requests):
    bmiform=BMIform()
    userdetailform=UserDetailForm
    bmi=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)

    if requests.method=='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
        bmiform=BMIform(requests.POST)
        if bmiform.is_valid():
            bmiform.save()
            numerator=float(requests.POST.get('weight'))
            denominator=float(requests.POST.get('height'))*float(requests.POST.get('height'))
            bmi=numerator/denominator
            requests.session['bmi']=bmi

    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("BMI-Email needs to be sent")
        print(requests.session['bmi'])
    """Sending Mail Ends"""

    bmiJSON=dumps({
        'bmi':bmi
    },default=str)

    context={'bmi_result':bmiJSON,'bmi':bmi,'userdetailform':userdetailform}

    return render(requests,'calculators/BMI.html',context)

def Water(requests):
    water_form=WaterForm()
    userdetailform=UserDetailForm()
    ans=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)

    if requests.method =='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
        water_form=WaterForm(requests.POST)
        if water_form.is_valid():
            water_form.save()
            weight=float(requests.POST.get('weight'))
            time=float(requests.POST.get('exercise_time'))
            F1=weight*0.044
            F2=(time/30)*0.355
            ans=F1+F2
            requests.session['water']=ans

    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("Water-Email needs to be sent")
        print(requests.session['water'])
    """Sending Mail Ends"""

    waterJSON=dumps({
        'water':ans
    },default=str)

    context={'water_result':waterJSON,'water':ans,'userdetailform':userdetailform}
    return render(requests,'calculators/water.html',context)

def WHR(requests):
    whr_form=WHRform()
    userdetailform=UserDetailForm()
    whr=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)
    
    if requests.method=='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
        whr_form=WHRform(requests.POST)
        if whr_form.is_valid():
            whr_form.save()
            num=float(requests.POST.get('waist'))
            den=float(requests.POST.get('hip'))
            whr=num/den
            requests.session['whr']=whr

    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("Waist to Hip Ratio-Email needs to be sent")
        print(requests.session['water'])
    """Sending Mail Ends"""

    whrJSON=dumps({
        'whr':whr
    })

    context={'whr_result':whrJSON,'whr':whr,'userdetailform':userdetailform}
    return render(requests,'calculators/WHR.html',context)

def BMR(requests):
    bmr_form=BMRform()
    userdetailform=UserDetailForm()
    bmr=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)

    if requests.method=='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
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

            requests.session['bmr']=bmr

    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("Basal Metabolic Rate-Email needs to be sent")
        print(requests.session['water'])
    """Sending Mail Ends"""

    bmrJSON=dumps({
        'bmr':bmr
    },default=str)
    context={'bmr_result':bmrJSON,'bmr':bmr,'userdetailform':userdetailform}
    return render(requests,'calculators/BMR.html',context)

def CalMacroNutri(requests):
    nutri_form=NutriForm()
    userdetailform=UserDetailForm()
    bmr=0
    calorie=0
    protein=0
    carbohydrates=0
    fats=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)
        
    if requests.method=='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
        nutri_form=NutriForm(requests.POST)
        if nutri_form.is_valid():
            nutri_form.save()
            weight=float(requests.POST.get('weight'))
            height=float(requests.POST.get('height'))*2.5
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            lifestyle=requests.POST.get('lifestyle')

            if gender=="Male":
                bmr=655+(9.6*weight)+(1.8*height)-(4.7*age)
            elif gender=="Female":
                bmr=66+(13.7*weight)+(5*height)-(6.8*age)

            if lifestyle=="Sedentary":
                calorie=bmr*1.2
            elif lifestyle=="Lightly Active":
                calorie=bmr*1.375
            elif lifestyle=="Moderately Active":
                calorie=bmr*1.55
            elif lifestyle=="Very Active":
                calorie=bmr*1.725
            elif lifestyle=="Extra Active":
                calorie=bmr*1.9
            
            protein=calorie*0.4
            carbohydrates=calorie*0.3
            fats=calorie*0.3
            requests.session['calorie']=calorie
            requests.session['protein']=protein
            requests.session['carbohydrates']=carbohydrates
            requests.session['fats']=fats
    
    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("Calorie and Nutrients-Email needs to be sent")
        print(requests.session['water'])
    """Sending Mail Ends"""
                
    nutriJSON=dumps({
        'calorie':calorie,
        'protein':protein,
        'carbohydrates':carbohydrates,
        'fats':fats
    },default=str)
    context={'nutri_result':nutriJSON,'calorie':calorie,'userdetailform':userdetailform}
    return render(requests,'calculators/nutri.html',context)

def BF(requests):
    bf_form=BFform()
    userdetailform=UserDetailForm()
    body_fat_weight=0
    body_fat_percentage=0

    if requests.session.has_key('name') and requests.session.has_key('email_id') and requests.session.has_key('mobile_no'):
        values={
                'name':requests.session['name'],
                'email_id':requests.session['email_id'],
                'mobile_no':requests.session['mobile_no']
            }
        userdetailform=UserDetailForm(initial=values)

    if requests.method=='POST':
        requests.session['name']=requests.POST.get('name')
        requests.session['email_id']=requests.POST.get('email_id')
        requests.session['mobile_no']=requests.POST.get('mobile_no')
        changed_values={
            'name':requests.session['name'],
            'email_id':requests.session['email_id'],
            'mobile_no':requests.session['mobile_no']
        }
        userdetailform=UserDetailForm(initial=changed_values)
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
            
            requests.session['body_fat_weight']=body_fat_weight
            requests.session['body_fat_percentage']=body_fat_percentage

    """Sending Mail"""
    if requests.POST.get('send_email'):
        print("Basal Metabolic Rate-Email needs to be sent")
        print(requests.session['water'])
    """Sending Mail Ends"""


    bfJSON=dumps({
        'bfw':body_fat_weight,
        'bfp':body_fat_percentage,
    },default=str)
    context={'bf_result':bfJSON,'bfw':body_fat_weight,'bfp':body_fat_percentage,'userdetailform':userdetailform}
    return render(requests,'calculators/BF.html',context)