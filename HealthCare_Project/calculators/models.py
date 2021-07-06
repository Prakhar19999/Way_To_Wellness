from django.db import models

class UserDetail(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()

    def __str__(self):
        return self.name

class BMI(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    weight=models.FloatField()
    height_ft=models.FloatField()
    height_inches=models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Body Mass Index"

class Water(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    weight=models.FloatField()
    exercise_time=models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Water"

class WHR(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    waist=models.FloatField()
    hip=models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Waist To Hip Ratio"

class BMR(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    weight=models.FloatField()
    height_ft=models.FloatField()
    height_inches=models.FloatField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Basal Metabolic Rate"

class CalMacroNutri(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    weight=models.FloatField()
    height_ft=models.FloatField()
    height_inches=models.FloatField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    lifestyle=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Calorie and Macro Nutritients"

class BF(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.IntegerField()
    weight=models.FloatField()
    waist=models.FloatField()
    wrist=models.FloatField()
    hip=models.FloatField()
    forearm=models.FloatField()
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Body Fat"