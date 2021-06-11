from django.shortcuts import render
from .models import *

def home(requests):
    testimonials=Testimonials.objects.all()
    context={'testimonials':testimonials}
    return render(requests,'way_to_wellness/home_page.html',context)