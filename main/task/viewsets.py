from .models import TaskList, Attachment, Task
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TaskListSerializers,TaskSerializers, AttachmentSerializers
from .permissions import IsTaskListOwnerOrGetAndPostOnly, IsTaskOwnerOrGetAndPostOnly, IsAttachmentOwnerOrGetAndPostOnly

from django.contrib.auth.models import User

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
             mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsTaskListOwnerOrGetAndPostOnly,]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializers

class TasktViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTaskOwnerOrGetAndPostOnly,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    def get_queryset(self):
        queryset = super(TasktViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        u_queryset = queryset.filter(created_by=user_profile)
        return u_queryset

    
class AttachmenttViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
             mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAttachmentOwnerOrGetAndPostOnly,]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializers

