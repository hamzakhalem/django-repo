from .models import TaskList, Attachment, Task
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TaskListSerializers
from .permissions import IsTaskListOwnerOrGetAndPostOnly

from django.contrib.auth.models import User

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
             mixins.UpdateDestroyMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsTaskListOwnerOrGetAndPostOnly,]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializers
