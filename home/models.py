from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slider = models.ImageField(default=1, upload_to='home', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Slider"

class Collage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField( default=1, upload_to='collage', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Collage"

class We_offer(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    training_content = RichTextField(blank=True, null=True)
    weoffer_image = models.ImageField( default=1, upload_to='we-offer', blank=True, null=True)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "We offer"
        verbose_name_plural = "We offer"

class Ticker(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    ticker = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ticker"
