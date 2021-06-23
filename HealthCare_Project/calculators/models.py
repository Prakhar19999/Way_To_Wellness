from django.db import models

class BMI(models.Model):
    weight=models.FloatField()
    height=models.FloatField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Body Mass Index"

class Water(models.Model):
    weight=models.FloatField()
    exercise_time=models.IntegerField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Water"

class WHR(models.Model):
    waist=models.FloatField()
    hip=models.FloatField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Waist To Hip Ratio"

class BMR(models.Model):
    weight=models.FloatField()
    height=models.FloatField()
    age=models.IntegerField()
    gender=models.BooleanField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Basal Metabolic Rate"

class CalMacroNutri(models.Model):
    weight=models.FloatField()
    height=models.FloatField()
    age=models.IntegerField()
    gender=models.BooleanField()
    lifestyle=models.TextField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Calorie and Macro Nutritients"

class BF(models.Model):
    weight=models.FloatField()
    waist=models.FloatField()
    wrist=models.FloatField()
    forearm=models.FloatField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Body Fat"