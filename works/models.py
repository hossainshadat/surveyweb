from django.db import models
import datetime


# Create your models here.

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Upcoming(models.Model):
    serial = models.IntegerField(blank=True, null=True)
    project_name = models.TextField( blank=True, null=True) #Textfield
    project_type = models.CharField(max_length=100, blank=True, null=True)
    time_period = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year)
    funding_agency = models.CharField(max_length=100,null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = "Upcoming work"

class Work_progress(models.Model):
    serial = models.IntegerField(blank=True, null=True)
    project_name = models.TextField( blank=True, null=True) #Textfield
    project_type = models.CharField(max_length=100, blank=True, null=True)
    time_period = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year)
    funding_agency = models.CharField(max_length=100,null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Work progress"
        verbose_name_plural = "Work in progress"

class Major_work(models.Model):
    serial = models.IntegerField(blank=True, null=True, unique=True)
    project_name = models.TextField( blank=True, null=True) #Textfield
    project_type = models.CharField(max_length=100, blank=True, null=True)
    time_period = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year)
    funding_agency = models.CharField(max_length=100,null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Major work"
        verbose_name_plural = "Major work"
