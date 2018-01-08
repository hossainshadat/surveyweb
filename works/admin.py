from django.contrib import admin
from .models import Upcoming, Work_progress, Major_work

# Register your models here.


admin.site.register(Major_work)
admin.site.register(Upcoming)
admin.site.register(Work_progress)
