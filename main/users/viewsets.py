from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import UserSerializers
from .permissions import IsUserOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializers