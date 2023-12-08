from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)  

admin.site.register(Blog, BlogAdmin)
