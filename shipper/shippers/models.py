from __future__ import unicode_literals

from django.contrib.gis.db import models

from shipper.users.models import User
# Create your models here.


class Shipper(User):
    shipper_location = models.PointField(srid=4326, dim=3, blank=True, null=True)
