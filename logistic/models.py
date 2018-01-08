from django.db import models

# Create your models here.

class Servicetype(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Servicetype maintitle"


class Subtitle(models.Model):
    servicetype = models.ForeignKey(Servicetype, on_delete=models.CASCADE, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.sub_title

    class Meta:
        verbose_name_plural = "Subtitle"


class Tool(models.Model):
    subtitle = models.ForeignKey(Subtitle, on_delete=models.CASCADE, blank=True, null=True)
    Equipement_name = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return self.Equipement_name

    class Meta:
        verbose_name_plural = "Tool"
