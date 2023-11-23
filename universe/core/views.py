from django.shortcuts import render
from .models import Main


def home(request):
    image =  Main.objects.first()
    context = {
        'image': image
    }

    return render(request, 'home/home.html', context)