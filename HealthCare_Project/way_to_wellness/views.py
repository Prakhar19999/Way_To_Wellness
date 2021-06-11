from django.shortcuts import render
from .models import *

def home(requests):
    testimonials=Testimonials.objects.all()
    carousel=Carousel.objects.all()
    services=Services.objects.all()

    context={
            'testimonials':testimonials,
            'carousel':carousel,
            'services':services,
            }

    return render(requests,'way_to_wellness/home_page.html',context)