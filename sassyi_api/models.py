from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
import django


class Device(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    owned_by = models.ForeignKey(User, on_delete=SET_NULL, null=True)


class Activity(models.Model):
    name = models.CharField(max_length=15, null=True)
    description = models.TextField(null=True)
    device = models.ForeignKey(Device, on_delete=SET_NULL, null=True)
    owned_by = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    start_time = models.DateTimeField(default=django.utils.timezone.now())
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name


class Scan(models.Model):
    device = models.ForeignKey(Device, on_delete=SET_NULL, null=True)
    activity = models.ForeignKey(Activity, on_delete=SET_NULL, null=True)
    scan_time = models.DateTimeField(auto_now_add=True)
