from jobs.models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('uid', 'status', 'pickup_location', 'drop_location', 'shipper', 'porters', 'time_to_reach', 'amount_offered', 'created_at')
