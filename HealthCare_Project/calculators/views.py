from django.shortcuts import render
from .models import *
from .forms import *
from json import dumps
from way_to_wellness.forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def calculators(requests):
    return render(requests,'calculators/calculator_base.html')

def BodyMassIndex(requests):
    bmiform=BMIform()
    userdetailform=UserDetailForm
    bmi=0
    weight=0
    height_ft=0
    height_inches=0
    height=0

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
            weight=float(requests.POST.get('weight'))
            height_ft=float(requests.POST.get('height_ft'))
            height_inches=float(requests.POST.get('height_inches'))
            height=(height_ft*0.3048)+(height_inches*0.0254)
            denominator=height*height
            bmi=weight/denominator
            user_bmi=BMI.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    weight=weight,
                                    height_ft=height_ft,
                                    height_inches=height_inches)
            user_bmi.save()
            requests.session['bmi']=bmi

            requests.session['weight']=weight
            requests.session['height_inches']=height_inches
            requests.session['height_ft']=height_ft
            requests.session['exercise_time']=0
            requests.session['waist']=0
            requests.session['hip']=0
            requests.session['age']=0
            requests.session['gender']=0
            requests.session['lifestyle']=0
            requests.session['wrist']=0
            requests.session['forearm']=0

    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['bmi'],
                                            'bmi':1,
                                            'weight': requests.session['weight'],
                                            'height_ft':requests.session['height_ft'],
                                            'height_inches':requests.session['height_inches'],
                                            'content':'Your calculated Body Mass Index'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()

    bmiJSON=dumps({
        'bmi':bmi
    },default=str)

    context={'bmi_result':bmiJSON,'bmi':bmi,'userdetailform':userdetailform}

    return render(requests,'calculators/BMI.html',context)

def WaterCalculator(requests):
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
            weight=float(requests.POST.get('weight'))
            time=float(requests.POST.get('exercise_time'))
            F1=weight*0.044
            F2=(time/30)*0.355
            ans=F1+F2
            user_water=Water.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    weight=weight,
                                    exercise_time=time)
            user_water.save()
            requests.session['water']=ans

            requests.session['weight']=weight
            requests.session['height_inches']=0
            requests.session['height_ft']=0
            requests.session['exercise_time']=time
            requests.session['waist']=0
            requests.session['hip']=0
            requests.session['age']=0
            requests.session['gender']=0
            requests.session['lifestyle']=0
            requests.session['wrist']=0
            requests.session['forearm']=0

    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['water'],
                                            'water':1,
                                            'weight':requests.session['weight'],
                                            'exercise_time':requests.session['exercise_time'],
                                            'content':'Your calculated Water requirement'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()

    waterJSON=dumps({
        'water':ans
    },default=str)

    context={'water_result':waterJSON,'water':ans,'userdetailform':userdetailform}
    return render(requests,'calculators/water.html',context)

def WaistToHip(requests):
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
            num=float(requests.POST.get('waist'))
            den=float(requests.POST.get('hip'))
            whr=num/den
            user_whr=WHR.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    waist=num,
                                    hip=den)
            user_whr.save()
            requests.session['whr']=whr
            
            requests.session['weight']=0
            requests.session['height_inches']=0
            requests.session['height_ft']=0
            requests.session['exercise_time']=0
            requests.session['waist']=num
            requests.session['hip']=den
            requests.session['age']=0
            requests.session['gender']=0
            requests.session['lifestyle']=0
            requests.session['wrist']=0
            requests.session['forearm']=0


    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['whr'],
                                            'whr':1,
                                            'waist':requests.session['waist'],
                                            'hip':requests.session['hip'],
                                            'content':'Your calculated Waist To Hip Ratio'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()

    whrJSON=dumps({
        'whr':whr
    })

    context={'whr_result':whrJSON,'whr':whr,'userdetailform':userdetailform}
    return render(requests,'calculators/WHR.html',context)

def BasalMetabolicRate(requests):
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
            weight=float(requests.POST.get('weight'))
            height_ft=float(requests.POST.get('height_ft'))
            height_inches=float(requests.POST.get('height_inches'))
            height=(height_ft*30.48)+(height_inches*2.54)
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            if gender=="Female":
                bmr=655+(9.6*weight)+(1.8*height)-(4.7*age)
            else:
                bmr=66+(13.7*weight)+(5*height)-(6.8*age)
            user_bmr=BMR.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    weight=weight,
                                    height_ft=height_ft,
                                    height_inches=height_inches,
                                    age=age,
                                    gender=gender)
            user_bmr.save()
            requests.session['bmr']=bmr
            
            requests.session['weight']=weight
            requests.session['height_inches']=height_inches
            requests.session['height_ft']=height_ft
            requests.session['exercise_time']=0
            requests.session['waist']=0
            requests.session['hip']=0
            requests.session['age']=age
            requests.session['gender']=gender
            requests.session['lifestyle']=0
            requests.session['wrist']=0
            requests.session['forearm']=0

    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['bmr'],
                                            'bmr':1,
                                            'weight': requests.session['weight'],
                                            'height_ft':requests.session['height_ft'],
                                            'height_inches':requests.session['height_inches'],
                                            'age':requests.session['age'],
                                            'gender':requests.session['gender'],
                                            'content':'Your calculated Basal Metabolic Rate'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()

    bmrJSON=dumps({
        'bmr':bmr
    },default=str)

    context={'bmr_result':bmrJSON,'bmr':bmr,'userdetailform':userdetailform}
    return render(requests,'calculators/BMR.html',context)

def Calorie(requests):
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
            weight=float(requests.POST.get('weight'))
            height_ft=float(requests.POST.get('height_ft'))
            height_inches=float(requests.POST.get('height_inches'))
            height=(height_ft*30.48)+(height_inches*2.54)
            age=float(requests.POST.get('age'))
            gender=requests.POST.get('gender')
            lifestyle=requests.POST.get('lifestyle')

            if gender=="Female":
                bmr=655+(9.6*weight)+(1.8*height)-(4.7*age)
            elif gender=="Male":
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
            user_calorie=CalMacroNutri.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    weight=weight,
                                    height_ft=height_ft,
                                    height_inches=height_inches,
                                    age=age,
                                    gender=gender,
                                    lifestyle=lifestyle)

            user_calorie.save()
            requests.session['calorie']=calorie
            requests.session['protein']=protein
            requests.session['carbohydrates']=carbohydrates
            requests.session['fat']=fats
            
            requests.session['weight']=weight
            requests.session['height_inches']=height_inches
            requests.session['height_ft']=height_ft
            requests.session['exercise_time']=0
            requests.session['waist']=0
            requests.session['hip']=0
            requests.session['age']=age
            requests.session['gender']=gender
            requests.session['lifestyle']=lifestyle
            requests.session['wrist']=0
            requests.session['forearm']=0
    
    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['calorie'],
                                            'nutri':1,
                                            'weight': requests.session['weight'],
                                            'height_ft':requests.session['height_ft'],
                                            'height_inches':requests.session['height_inches'],
                                            'age':requests.session['age'],
                                            'gender':requests.session['gender'],
                                            'lifestyle':requests.session['lifestyle'],
                                            'fat':requests.session['fat'],
                                            'carbohydrates':requests.session['carbohydrates'],
                                            'protein':requests.session['protein'],
                                            'content':'Your calculated Calorie requirement'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()
                
    nutriJSON=dumps({
        'calorie':calorie,
        'protein':protein,
        'carbohydrates':carbohydrates,
        'fats':fats
    },default=str)

    context={'nutri_result':nutriJSON,'calorie':calorie,'userdetailform':userdetailform}
    return render(requests,'calculators/nutri.html',context)

def BodyFat(requests):
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
            weight=float(requests.POST.get('weight'))
            waist=float(requests.POST.get('waist'))
            wrist=float(requests.POST.get('wrist'))
            hip=float(requests.POST.get('hip'))
            forearm=float(requests.POST.get('forearm'))
            gender=requests.POST.get('gender')
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
            user_bf=BF.objects.create(name=requests.session['name'],
                                    email_id=requests.session['email_id'],
                                    mobile_no=requests.session['mobile_no'],
                                    weight=weight,
                                    waist=waist,
                                    wrist=wrist,
                                    hip=hip,
                                    forearm=forearm,
                                    gender=gender)
            user_bf.save()
            requests.session['bf']=body_fat_weight
            requests.session['bfp']=body_fat_percentage

            requests.session['weight']=weight
            requests.session['height_inches']=0
            requests.session['height_ft']=0
            requests.session['exercise_time']=0
            requests.session['waist']=waist
            requests.session['hip']=hip
            requests.session['age']=0
            requests.session['gender']=gender
            requests.session['lifestyle']=0
            requests.session['wrist']=wrist
            requests.session['forearm']=forearm

    if requests.POST.get('send_email'):
        send_mail=requests.session['email_id']
        html_content=render_to_string("email/result_email.html",
                                            {'name':requests.session['name'],
                                            'email_id':requests.session['email_id'],
                                            'mobile_no':requests.session['mobile_no'],
                                            'value':requests.session['bf'],
                                            'bfp':requests.session['bfp'],
                                            'bf':1,
                                            'weight': requests.session['weight'],
                                            'waist':requests.session['waist'],
                                            'hip':requests.session['hip'],
                                            'age':requests.session['age'],
                                            'gender':requests.session['gender'],
                                            'wrist':requests.session['wrist'],
                                            'forearm':requests.session['forearm'],
                                            'content':'Your calculated Body Fat Weight'})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            #subject
            'Way To Wellness',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
        email.attach_alternative(html_content,"text/html")
        email.send()


    bfJSON=dumps({
        'bfw':body_fat_weight,
        'bfp':body_fat_percentage,
    },default=str)

    context={'bf_result':bfJSON,'bfw':body_fat_weight,'bfp':body_fat_percentage,'userdetailform':userdetailform}
    return render(requests,'calculators/BF.html',context)