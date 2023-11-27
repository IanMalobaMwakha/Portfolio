from django.shortcuts import render
from core.models import Home
from .models import Blog
from django.shortcuts import render, get_object_or_404


def index(request):
    official_image = Home.objects.get()
    blogs = Blog.objects.all()

    return render(request, "blogs/index.html", {
        "official_image": official_image,
        'blogs': blogs
    })

def blog_body(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    official_image = Home.objects.get()

    return render(request, "blogs/blog_body.html", {
        "official_image": official_image,
        'blog': blog,
        'pk': pk,
    })



