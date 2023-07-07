from django.db import models

class Home(models.Model):
    background_image = models.ImageField(upload_to='home_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    