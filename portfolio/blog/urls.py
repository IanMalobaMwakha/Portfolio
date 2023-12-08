from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<slug:slug>/', views.blog_body, name='blog_body'),
]

