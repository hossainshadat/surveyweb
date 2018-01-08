from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slider = models.ImageField(default=1, upload_to='we-offer', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Slider"

class Training(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    training_content = RichTextField(blank=True, null=True)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name_plural = "Training"

class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    gallery_image = models.ImageField( default=1, upload_to='we-offer', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gallery"

