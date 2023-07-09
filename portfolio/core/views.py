from django.shortcuts import render
from django.conf import settings


from .models import Home

def index(request):
    background_image = Home.objects.get()
    name = Home.objects.get()
    official_image = Home.objects.get()

    return render(request, 'core/index.html', {
        'background_image': background_image,
        'name': name,
        'official_image': official_image,
    })