from rest_framework import viewsets
from .models import Device, Activity, Scan
from .serializers import DeviceSerializer, ActivitySerializer, ScanSerializer


class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ScanView(viewsets.ModelViewSet):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer
