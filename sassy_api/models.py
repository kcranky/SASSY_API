from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver


class Activity(models.Model):
    """
    An activity can occur once (at an instant - i.e. only have a start time)
    It can occur over a duration (have a start and end time)
    """
    name = models.CharField(max_length=15, null=True)
    description = models.TextField(null=True)
    created_by = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        if self.name is None:
            return "NULLNAME"
        return "{} - {}".format(self.name, self.description[:20])


class Device(models.Model):
    """
    Keeps track of devices
    """
    id = models.CharField(max_length=20, primary_key=True)
    owned_by = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    current_activity = models.ForeignKey(Activity, on_delete=SET_NULL, null=True)


class Card(models.Model):
    """
    Holds data on cards
    It is assumed this data will be able to be parsed by an ICTS API call
    """
    card_id = models.CharField(max_length=25, null=False, unique=True)


class Scan(models.Model):
    """
    Holds a record of all scans
    Scans assume a card, device, activity and time
    """
    device = models.ForeignKey(Device, on_delete=SET_NULL, null=True, blank=True)
    activity = models.ForeignKey(Activity, on_delete=SET_NULL, null=True)
    card = models.ForeignKey(Card, on_delete=SET_NULL, null=True)
    scan_time = models.DateTimeField(blank=True, null=True)


class Profile(models.Model):
    """
    Extends the "user" by adding a linked card
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=SET_NULL, null=True)
