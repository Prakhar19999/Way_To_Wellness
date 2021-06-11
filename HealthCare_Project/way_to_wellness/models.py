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