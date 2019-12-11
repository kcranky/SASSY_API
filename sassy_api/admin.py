"""
    Register admin sites
"""
from django.contrib import admin
from .models import Device, Activity, Scan, Card, Profile

admin.site.register(Device)
admin.site.register(Activity)
admin.site.register(Scan)
admin.site.register(Card)
admin.site.register(Profile)

