from django.shortcuts import render
from .models import *
from .forms import *

def home(requests):
   form=AppointmentForm()
   if requests.method == "POST":
      form=AppointmentForm(requests.POST)
      if form.is_valid():
         print(requests.POST)
   form=AppointmentForm()
   testimonials=Testimonials.objects.all()
   carousel=Carousel.objects.all()
   services=Services.objects.all()
   about=AboutUs.objects.all()
   context={
         'testimonials':testimonials,
         'carousel':carousel,
         'services':services,
         'about':about,
         'ap_form':form,
      }

   return render(requests,'way_to_wellness/home_page.html',context)