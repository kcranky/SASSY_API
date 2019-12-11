"""
    Sassy API URL Configuration
"""

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('devices', views.DeviceView)
router.register('activities', views.ActivityView)
router.register('scans', views.ScanView)
router.register('cards', views.CardView)
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('get_staff_activities/<slug:card_id>', views.get_staff_activities, name='test')
]
