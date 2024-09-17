from .models import TaskList, Attachment, Task, COMPLETE, NOT_COMPLETE
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TaskListSerializers,TaskSerializers, AttachmentSerializers
from .permissions import IsTaskListOwnerOrGetAndPostOnly, IsTaskOwnerOrGetAndPostOnly, IsAttachmentOwnerOrGetAndPostOnly

from django.contrib.auth.models import User
from django.utils import timezone


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
    @action(detail=True, method= ['post'],)
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']
            if(status == NOT_COMPLETE):
                if(task.status == COMPLETE):
                    task.status = NOT_COMPLETE 
                    task.completed_on = None
                    task.completed_by = None
            else:
                if(task.status == NOT_COMPLETE):
                    task.status = COMPLETE 
                    task.completed_on = timezone.now()
                    task.completed_by = profile

            task.save()
            serilzers = TaskSerializers(instance=task, context = {'request': request})
            return serilzers


        except Exception as e:
            pass    

        


    
class AttachmenttViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
             mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAttachmentOwnerOrGetAndPostOnly,]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializers

