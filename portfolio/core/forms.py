from django import forms
from .models import Project

class ProjectDescriptionForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_description',)
