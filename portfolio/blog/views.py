from django.shortcuts import render
from core.models import Home

def index(request):
    official_image = Home.objects.get()

    return render(request, "blogs/index.html", {
        "official_image": official_image,
    })

