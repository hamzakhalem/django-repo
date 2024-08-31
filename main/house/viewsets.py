from .models import House
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import HouseSerializers
from .permissions import IsHouseOwnerOrGetAndPostOnly


class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsHouseOwnerOrGetAndPostOnly,]
    queryset = House.objects.all()
    serializer_class = HouseSerializers
    
    @action(detail=True, methods=['post'], name='join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if(user_profile.house == None):
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif user_profile in house.members.all():
                return Response({'details': 'already in house'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'details': 'already in another house'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
    
    @action(detail=True, methods=['post'], name='leave', permission_classes = [])
    def leave(self, request, pk=None):
        try: 
            house = self.get_object()
            user_profile = request.user.profile
            if user_profile in house.members.all():
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'details': 'not in house'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR) 