from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('devices', views.DeviceView)
router.register('activities', views.ActivityView)
router.register('scans', views.ScanView)

urlpatterns = [
    path('', include(router.urls))
]
