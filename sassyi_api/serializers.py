from rest_framework import serializers
from .models import Device, Activity, Scan, Card
from django.contrib.auth.models import User


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'current_activity', 'url')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.URLField(read_only=True)

    class Meta:
        model = Activity
        fields = ('url', 'name', 'created_by', 'description', 'start_time', 'end_time')

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        print(request.data)
        print(validated_data)
        a = Activity.objects.create(description=validated_data['description'], start_time=validated_data['start_time'], end_time=validated_data['end_time'])
        a.created_by = user
        a.save()
        return a


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
        fields = '__all__'
