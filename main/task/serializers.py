from rest_framework import serializers
from .models import TaskList, Attachment, Task
from house.models import House

class TaskListSerializers(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many= False, view_name = 'house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name = 'profile-detail')
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name = 'task-detail')
    class Meta:
        model= TaskList
        fields =['url', 'id', 'name', 'created_on', 'created_by', 'house', 'description', 'status', 'tasks'  ]
        read_only_fields = ['created_on', 'status', 'notcompleted_tasks_count']


class TaskSerializers(serializers.ModelSerializer):

    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name = 'profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name = 'profile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset= TaskList.objects.all(), many=False, view_name = 'tasklist-detail')
    attachments = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name = 'attachment-detail')


    class Meta:
        model= Task
        fields =['url', 'id', 'name', 'created_on', 'completed_on', 'created_by', 'completed_by',
                 'description', 'status', 'task_lis', 'attachments'  ]
        read_only_fields = ['created_on', 'completed_on', 'created_by', 'completed_by',
                            'status', 'notcompleted_tasks_count']
    

class AttachmentSerializers(serializers.ModelSerializer):
    
    task_list = serializers.HyperlinkedRelatedField(queryset= Task.objects.all(), many=False, view_name = 'task-detail')
    class Meta:
        model= Task
        fields =['url', 'id', 'data', 'created_on', 'task']
        read_only_fields = ['created_on']