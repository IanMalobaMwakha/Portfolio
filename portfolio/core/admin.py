from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


from .models import Home, About, SkillCategory, Skill, Education, Experience, ToolsUsed, Project

admin.site.register(Home)

admin.site.register(About)

admin.site.register(SkillCategory)

admin.site.register(Skill)

admin.site.register(Education)

admin.site.register(Experience)

admin.site.register(ToolsUsed)

admin.site.register(Project)


