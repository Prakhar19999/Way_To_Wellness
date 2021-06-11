from django.shortcuts import render
from .models import *

def home(requests):
    testimonials=Testimonials.objects.all()
    carousel=Carousel.objects.all()

    context={
            'testimonials':testimonials,
            'carousel':carousel
            }

    return render(requests,'way_to_wellness/home_page.html',context)