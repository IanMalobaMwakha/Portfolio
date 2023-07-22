from django.shortcuts import render
from django.conf import settings


from .models import Home, About, Skill, SkillCategory, Education

def index(request):
    #Home
    name = Home.objects.get()
    official_image = Home.objects.get()
    #About
    unofficial_image = About.objects.get()
    #Skills
    skills = Skill.objects.all()
    skillcategories = SkillCategory.objects.all()
    #Resume
    major_name = Education.objects.all()
    school_name = Education.objects.all()
    school_location = Education.objects.all()
    time_period = Education.objects.all()


    return render(request, 'core/index.html', {
        'name': name,
        'official_image': official_image,
        'unofficial_image': unofficial_image,
        'skills': skills,
        'skillcategories': skillcategories,
        'major_name': major_name,
        'school_name': school_name,
        'school_location': school_location,
        'time_period': time_period,
    })


