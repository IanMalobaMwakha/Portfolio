
from django.db import models

# HOME
class Home(models.Model):
    name = models.CharField(max_length=255)
    official_image = models.ImageField(upload_to='home_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Home Section"

# ABOUT  
class About(models.Model):
    unofficial_image = models.ImageField(upload_to='about_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Section"

# SKILLS

class SkillCategory(models.Model):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Skill Section: Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    skillcategory = models.ForeignKey(SkillCategory, related_name='skills', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Skill Section: Skills"

    def __str__(self):
        return self.name
    

# RESUME
class Education(models.Model):
    major_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Resume Section: Education"

    def __str__(self):
        return self.major_name

class Experience(models.Model):
    work_name = models.CharField(max_length=255)
    work_mode = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    work_description = models.TextField()
    period = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Resume Section: Work Experience"

    def __str__(self):
        return self.work_name


