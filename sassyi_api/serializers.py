from rest_framework import serializers
from .models import Device, Activity, Scan, Card
from django.contrib.auth.models import User


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'url')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('url', 'created_by', 'start_time', 'end_time')


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ('device', 'url', 'activity', 'scan_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('url', 'card_id')
