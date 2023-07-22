
from django.db import models

# HOME
class Home(models.Model):
    name = models.CharField(max_length=255)
    official_image = models.ImageField(upload_to='home_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Home"

# ABOUT  
class About(models.Model):
    unofficial_image = models.ImageField(upload_to='about_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About"

# SKILLS

class SkillCategory(models.Model):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    skillcategory = models.ForeignKey(SkillCategory, related_name='skills', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# RESUME
class Resume(models.Model):
    major_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Resume"

    def __str__(self):
        return self.major_name


