from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    blog_name = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    # date
    body = RichTextUploadingField()
    def __str__(self):
        return self.blog_name
    
    class Meta:
        verbose_name_plural = "BLOGS SECTION"