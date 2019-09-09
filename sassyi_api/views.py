from rest_framework import viewsets
from .models import Device, Activity, Scan, User
from .serializers import DeviceSerializer, ActivitySerializer, ScanSerializer, UserSerializer
from rest_framework.response import Response

class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ScanView(viewsets.ModelViewSet):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()