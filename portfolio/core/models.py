from django.db import models

class Home(models.Model):
    background_image = models.ImageField(upload_to='home_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    official_image = models.ImageField(upload_to='home_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
class About(models.Model):
    unofficial_image = models.ImageField(upload_to='about_images', blank=True, null=True)

    def __str__(self):
        return self.unofficial_image



from django.db import models

class Skill(models.Model):
    SKILL_TYPE_CHOICES = (
        ('professional', 'Professional'),
        ('personal', 'Personal'),
    )

    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPE_CHOICES)

    def __str__(self):
        return self.name
