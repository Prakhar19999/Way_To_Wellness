from django.db import models

class Testimonials(models.Model):
    name=models.TextField(max_length=30)
    profession=models.TextField(max_length=500)
    statement=models.TextField()
    image=models.ImageField(upload_to='landing_page_testimonials/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Testimonials'

class Carousel(models.Model):
    heading=models.TextField()
    quote=models.TextField()
    button_name=models.TextField()
    image=models.ImageField(upload_to='landing_page_carousel/')

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name_plural='Carousel'

class Services(models.Model):
    title1=models.TextField()
    paragraph1=models.TextField()
    image1=models.ImageField(upload_to='landing_page_services/')
    title2=models.TextField()
    paragraph2=models.TextField()
    image2=models.ImageField(upload_to='landing_page_services/')
    title3=models.TextField()
    paragraph3=models.TextField()
    image3=models.ImageField(upload_to='landing_page_services/')

    class Meta:
        verbose_name_plural='Services'