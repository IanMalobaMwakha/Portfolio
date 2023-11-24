from django.shortcuts import render
from core.models import Home
from .models import Blog

def index(request):
    official_image = Home.objects.get()
    blogs = Blog.objects.all()

    return render(request, "blogs/index.html", {
        "official_image": official_image,
        'blogs': blogs
    })

