from django.db import models
import datetime

# Create your models here.

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class Organization_abstract(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    gallery_image = models.ImageField(max_length=100, default=1, upload_to='organization', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Organization abstract"
        verbose_name_plural = "Organization abstract"


class Human_resource(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField( blank=True, null=True)
    image = models.ImageField(max_length=100, default=1, upload_to='member')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Human resource"
        verbose_name_plural = "Human resource"

class Report(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.IntegerField(('start'), choices=YEAR_CHOICES, blank=True, null=True,
                               default=datetime.datetime.now().year)
    end_year = models.IntegerField(('end'), choices=YEAR_CHOICES, blank=True, null=True,
                               default=datetime.datetime.now().year)

    def __str__(self):
        return self.title


class Audit_report(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    beginning_year = models.IntegerField(('beginning'), choices=YEAR_CHOICES, blank=True, null=True,
                                     default=datetime.datetime.now().year)
    ending_year = models.IntegerField(('latest'), choices=YEAR_CHOICES, blank=True, null=True,
                                   default=datetime.datetime.now().year)
    year = models.ForeignKey(Report, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Audit report"
        verbose_name_plural = "Audit report"
