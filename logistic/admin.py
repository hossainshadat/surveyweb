from django.contrib import admin
from .models import Tool, Subtitle, Servicetype

# Register your models here.

admin.site.register(Servicetype)
admin.site.register(Subtitle)
admin.site.register(Tool)