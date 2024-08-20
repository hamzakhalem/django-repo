from django.contrib.auth.models import User
from .models import Profile
from rest_framework import viewsets
from .serializers import UserSerializers, ProfileSerializers
from .permissions import IsUserOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializers
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers