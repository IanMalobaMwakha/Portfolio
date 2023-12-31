from django.db import models


# HOME
class Home(models.Model):
    name = models.CharField(max_length=255)
    official_image = models.ImageField(upload_to='home_images', blank=True, null=True)
    logo = models.ImageField(upload_to='home_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "HOME SECTION"

# ABOUT  
class About(models.Model):
    unofficial_image = models.ImageField(upload_to='about_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = "ABOUT SECTION"
    
    def __str__(self):
        return "Unofficial Image"

# SKILLS

class SkillCategory(models.Model):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "SKILL SECTION: Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    skillcategory = models.ForeignKey(SkillCategory, related_name='skills', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "SKILL SECTION: Skills"

    def __str__(self):
        return self.name
    

# RESUME
class Education(models.Model):
    major_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)
    education_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "RESUME SECTION: Education"
        ordering = ["-created_at"]

    def __str__(self):
        return self.major_name

class Experience(models.Model):
    work_name = models.CharField(max_length=255)
    work_mode = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    work_description = models.TextField(null=   True, blank=True)
    period = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "RESUME SECTION: Work Experience"
        ordering = ["-created_at"]

    def __str__(self):
        return self.work_name


# PROJECTS
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255, null=True, blank=True)
    live_link = models.CharField(max_length=255, null=True, blank=True)
    github_readme_link = models.CharField(max_length=255, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_images', blank=True, null=True)
    project_short_description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    
    class Meta:
        verbose_name_plural = "PROJECTS SECTION"
        # ordering = ["-created_at"]

    def __str__(self):
        return self.project_name
    

class Contact(models.Model):
    my_email = models.CharField(max_length=255, null=True, blank=True)
    my_phone = models.CharField(max_length=255, null=True, blank=True)
    linkedln = models.CharField(max_length=255, null=True, blank=True)
    github= models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    codepen = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "CONTACT SECTION: Contact"

    def __str__(self):
        return "My Contact"


