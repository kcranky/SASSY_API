from rest_framework import serializers
from .models import Device, Activity, Scan


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'url')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('device', 'url', 'owned_by', 'start_time', 'end_time')


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ('device', 'url', 'activity', 'scan_time')
