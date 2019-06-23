from django.contrib import admin
from .models import Device, Activity, Scan

admin.site.register(Device)
admin.site.register(Activity)
admin.site.register(Scan)
