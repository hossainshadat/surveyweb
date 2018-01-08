from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Survey_detail(models.Model):
    title = RichTextField( blank=True, null=True)
    project_type = models.CharField(max_length=100, blank=True, null=True)
    survey_tag = models.CharField(max_length=100, null=True, blank=True)
    last_update = models.DateField(auto_now=False, auto_now_add=False)
    project_description = RichTextField( blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Survey detail"
        verbose_name_plural = "Survey detail"

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    gallery_image = models.ImageField( default=1, upload_to='survey-detail', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

class Publication_link(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    publication_link = RichTextField( blank=True, null=True)
    location = models.ImageField(default=1, upload_to='survey-detail', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publication link"
        verbose_name_plural = "Publication link"
