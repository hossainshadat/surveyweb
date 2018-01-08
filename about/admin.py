from django.contrib import admin
from .models import Organization_abstract, Human_resource, Report, Audit_report

# Register your models here.
admin.site.register(Organization_abstract)
admin.site.register(Human_resource)
admin.site.register(Report)
admin.site.register(Audit_report)
# Register your models here.
