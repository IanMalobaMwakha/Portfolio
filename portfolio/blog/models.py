from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.text import slugify


class Blog(models.Model):
    blog_name = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    blog_date = models.CharField(max_length=255, blank= True, null=True)
    blog_read_time = models.IntegerField(blank= True, null=True)
    blog_card_intro = models.CharField(max_length=100, blank= True, null=True)
    body = RichTextUploadingField()
    blog_date_for_ordering = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.blog_name
    
    class Meta:
        ordering = ['-blog_date_for_ordering']
        verbose_name_plural = "BLOGS SECTION"


