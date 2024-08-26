from .models import House
from rest_framework import viewsets, mixins
from .serializers import HouseSerializers
from .permissions import IsHouseOwnerOrGetAndPostOnly


class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsHouseOwnerOrGetAndPostOnly,]
    queryset = House.objects.all()
    serializer_class = HouseSerializers