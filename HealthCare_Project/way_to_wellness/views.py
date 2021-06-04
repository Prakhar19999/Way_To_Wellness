from django.shortcuts import render


def home(requests):
    return render(requests,'way_to_wellness/home_page.html')