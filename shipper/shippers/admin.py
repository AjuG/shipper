from django.contrib import admin

# Register your models here.
from shippers.models import Shipper


class ShipperAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shipper, ShipperAdmin)
