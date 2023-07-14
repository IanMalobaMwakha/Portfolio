from django.contrib import admin

from .models import Home, About, Skill

admin.site.register(Home)

admin.site.register(About)


class SubSkillInline(admin.StackedInline):
    model = Skill
    extra = 1
    fk_name = 'parent_skill'
    verbose_name_plural = 'Subskills'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type')
    list_filter = ('skill_type',)
    search_fields = ('name',)
    inlines = [SubSkillInline]

admin.site.register(Skill, SkillAdmin)
