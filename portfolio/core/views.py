from django.shortcuts import render
from django.conf import settings


from .models import Home, About, Skill, SkillCategory

def index(request):
    background_image = Home.objects.get()
    name = Home.objects.get()
    official_image = Home.objects.get()

    return render(request, 'core/index.html', {
        'background_image': background_image,
        'name': name,
        'official_image': official_image,
    })


def about(request):
    unofficial_image = About.objects.get()

    return render(request, 'core/index.html', {
        'unofficial_image': unofficial_image,
    })


def skills(request):
    skills = Skill.objects.all()
    skillcategories = SkillCategory.objects.all()

    return render(request, 'core/index.html', {
        'skills': skills,
        'skillcategories': skillcategories,
    })

