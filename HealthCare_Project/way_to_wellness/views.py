from django.shortcuts import render
from .models import *
from .forms import *

def home(requests):
   form=AppointmentForm()
   if requests.method == "POST":
      form=AppointmentForm(requests.POST)
      if form.is_valid():
         form.save()
   form=AppointmentForm()
   testimonials=Testimonials.objects.all()
   carousel=Carousel.objects.all().first()
   carousel_items=[]
   for items in Carousel.objects.all():
      carousel_items.append(items)
   if len(carousel_items)>0:
      carousel_items.pop(0)
   services=Services.objects.all()
   about=AboutUs.objects.all()
   context={
         'testimonials':testimonials,
         'carousel':carousel,
         'services':services,
         'about':about,
         'ap_form':form,
         'carousel_items':carousel_items,
      }

   return render(requests,'way_to_wellness/home_page.html',context)