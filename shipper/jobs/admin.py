from django.contrib import admin

from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)

# Register your models here.
