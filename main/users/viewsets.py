from django.contrib.auth.models import User
from .models import Profile
from rest_framework import viewsets, mixins
from .serializers import UserSerializers, ProfileSerializers
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializers
class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsProfileOwnerOrGetAndPostOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers