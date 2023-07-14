from django.shortcuts import render
from django.conf import settings


from .models import Home, About, Skill

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
    professional_categories = Skill.objects.filter(skill_type='professional', parent_skill__isnull=True)
    personal_skills = Skill.objects.filter(skill_type='personal')

    context = {
        'professional_categories': professional_categories,
        'personal_skills': personal_skills
    }
    return render(request, 'core/index.html', context)
