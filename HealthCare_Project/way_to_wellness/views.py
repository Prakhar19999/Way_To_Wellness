from django.shortcuts import render
from .models import *

def home(requests):
    testimonials=Testimonials.objects.all()
    carousel=Carousel.objects.all()
    services=Services.objects.all()
    about=AboutUs.objects.all()

    context={
            'testimonials':testimonials,
            'carousel':carousel,
            'services':services,
            'about':about,
            }

    return render(requests,'way_to_wellness/home_page.html',context)