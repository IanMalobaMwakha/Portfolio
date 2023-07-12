from django.db import models

class Home(models.Model):
    background_image = models.ImageField(upload_to='home_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    official_image = models.ImageField(upload_to='home_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
class About(models.Model):
    unofficial_image = models.ImageField(uppload_to='about_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
