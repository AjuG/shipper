from django.contrib import admin

# Register your models here.
from porters.models import Porter


class PorterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Porter, PorterAdmin)
