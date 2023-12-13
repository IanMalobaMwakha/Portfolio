from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:slug>/', views.blog_body, name='blog_body'),
    path('search/', views.search_blogs, name='search_blogs'),  # Add this line for the search functionality

]

