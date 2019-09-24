from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status, permissions
from .models import Device, Activity, Scan, User, Card
from .serializers import DeviceSerializer, ActivitySerializer, ScanSerializer, UserSerializer, CardSerializer
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


class CardView(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = CardSerializer
    queryset = Card.objects.all()


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_staff_activities(request, card_id):
    try:
        user = User.objects.get(profile__card__card_id=card_id)
        if not user.is_staff:
            return Response({"message": "Card is not associated staff member"}, status=status.HTTP_401_UNAUTHORIZED)

        # we can assume here they have a card linked to staff

        data = Activity.objects.filter(created_by=user)
        if data.count() == 1:
            activities = ActivitySerializer(data)
        elif data.count() > 1:
            activities = ActivitySerializer(data, many=True)
        elif data.count() == 0:
            return Response({"message": "No events found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Hello, world!",
                         "username": user.username,
                         "activities": activities.data,
                         "card_id": card_id})

    except User.DoesNotExist:
        return Response({"message": "No user linked to card"}, status=status.HTTP_404_NOT_FOUND)
