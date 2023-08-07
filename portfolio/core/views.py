from django.shortcuts import render
from django.conf import settings
from .forms  import ProjectDescriptionForm

from django.shortcuts import get_object_or_404
from .models import Home, About, Skill, SkillCategory, Education, Experience, ToolsUsed, Project

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
    education_description = Education.objects.all()

    work_name = Experience.objects.all()
    work_mode = Experience.objects.all()
    company_name = Experience.objects.all()
    company_location = Experience.objects.all()
    work_description = Experience.objects.all()
    period = Experience.objects.all()

    # Projects
    project_name = Project.objects.all()
    github_link = Project.objects.all()
    live_link = Project.objects.all()
    project_image = Project.objects.all()
    project_short_description = Project.objects.all()
    project_description = Project.objects.all()
    tools_and_lang = Project.objects.all()
    tools_name = ToolsUsed.objects.all()



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
        'education_description': education_description,

        'work_name': work_name,
        'work_mode': work_mode,
        'company_name': company_name,
        'company_location': company_location,
        'work_description': work_description,
        'period': period,

        'project_name': project_name,
        'github_link': github_link,
        'live_link': live_link,
        'project_image': project_image,
        'project_short_description': project_short_description,
        'project_description': project_description,
        'tools_and_lang': tools_and_lang,
        'tools_name': tools_name,

    })


def project_detail(request, pk, project_name):
    project = get_object_or_404(Project, pk=pk)

    return render(request, 'core/project_detail.html', {
        'project': project,
        'pk': pk,
        'project_name': project_name,
    })

def project_description(request):
    form = ProjectDescriptionForm()

    return render(request, {
        'form': form
    })