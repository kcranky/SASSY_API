from rest_framework import serializers
from .models import Device, Activity, Scan, Card, Profile
from django.contrib.auth.models import User
from datetime import datetime


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'current_activity', 'owned_by', 'url')


class CardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
        extra_kwargs = {
            'card_id': {'validators': []},
        }


class ActivitySerializer(serializers.ModelSerializer):
    created_by = serializers.URLField(read_only=True)

    class Meta:
        model = Activity
        # fields = ('url', 'name', 'created_by', 'description', 'start_time', 'end_time')
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        a = Activity.objects.create(name=validated_data['name'], description=validated_data['description'], start_time=validated_data['start_time'], end_time=validated_data['end_time'])
        a.created_by = user
        a.save()
        return a


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    card = CardSerializer()

    class Meta:
        model = Scan
        fields = ('device', 'url', 'activity', 'card', 'scan_time')

    def create(self, validated_data):
        card_data = validated_data.pop('card')
        card, created = Card.objects.get_or_create(**card_data)
        print(card)
        scan, created = Scan.objects.update_or_create(
            activity=validated_data.get('activity', None), card=card,
            defaults={
                'device': validated_data.get('device', None),
                'activity': validated_data.get('activity', None),
                'card': card,
                'scan_time': datetime.now(),
            })
        return scan


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('card',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'profile', 'is_staff')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        profile, created = Profile.objects.get_or_create(user=user, **profile_data) # Already have a signal to do this?? Try get_or_create ?
        if created:
            profile.save()
        return user

    def update(self, instance, validated_data):
        # Update the  instance
        profile_data = validated_data.pop('profile')
        # first check if a profile exists, if not create one.
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        profile.card = profile_data.get(
            'card',
            profile.card
        )
        profile.save()

        return instance



