from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    about = About.objects.all().first()
    return render(
        request,
        'about/about_me.html',
        {"about": about},
    )