from django.shortcuts import render
from django.conf import settings


from .models import Home, About, Skill, SkillCategory

def index(request):
    name = Home.objects.get()
    official_image = Home.objects.get()
    unofficial_image = About.objects.get()
    skills = Skill.objects.all()
    skillcategories = SkillCategory.objects.all()


    return render(request, 'core/index.html', {
        'name': name,
        'official_image': official_image,
        'unofficial_image': unofficial_image,
        'skills': skills,
        'skillcategories': skillcategories,
    })


