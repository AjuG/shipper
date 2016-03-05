from __future__ import unicode_literals

from flufl.enum import IntEnum

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models

from shippers.models import Shipper
from porters.models import Porter

# Create your models here.


class JobStatusEnum(IntEnum):
    unknown = 0
    requested = 1
    booked = 2
    pickup = 3
    enroute = 4
    drop = 5
    fulfilled = 6


class Job(models.Model):
    STATUS_TYPE = [(int(enum_choice), enum_choice.name) for enum_choice in JobStatusEnum]
    uid = models.IntegerField(max_length=5)
    status = models.IntegerField(default=int(JobStatusEnum.unknown),
                                          choices=STATUS_TYPE,
                                          blank=True, null=True)
    pickup_location = models.PointField(srid=4326, dim=3, blank=True, null=True)
    drop_location = models.PointField(srid=4326, dim=3, blank=True, null=True)
    shipper = models.ForeignKey(Shipper)
    porters = models.ManyToManyField(Porter, blank=True, null=True)
    time_to_reach = models.IntegerField()
    amount_offered = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
