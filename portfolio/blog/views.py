from django.shortcuts import render
from core.models import Home, Contact
from .models import Blog
from django.shortcuts import render, get_object_or_404
from django.db.models import Q



def index(request):
    official_image = Home.objects.get()
    blogs = Blog.objects.all()
    my_email = Contact.objects.all()

    return render(request, "blogs/index.html", {
        "official_image": official_image,
        'blogs': blogs,
        "my_email": my_email
    })

def blog_body(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    official_image = Home.objects.get()
    my_email = Contact.objects.all()


    return render(request, "blogs/blog_body.html", {
        "official_image": official_image,
        'blog': blog,
        'slug': slug,
        "my_email": my_email
    })


def search_blogs(request):
    official_image = Home.objects.get()
    my_email = Contact.objects.all()


    if request.method == 'POST':
        search_query = request.POST.get('search_query')

        # Use Q objects to search in multiple fields
        posts = Blog.objects.filter(
            Q(blog_name__icontains=search_query) |
            Q(blog_card_intro__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(slug__icontains=search_query)
        )

        return render(request, 'blogs/index.html', {
            'query': search_query, 
            "official_image": official_image,
            'posts': posts,
            "my_email": my_email
            })
    else:
        return render(request, 'blogs/index.html', {})


