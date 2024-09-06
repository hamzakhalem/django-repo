from rest_framework import serializers
from .models import TaskList
from house.models import House

class TaskListSerializers(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many= False, view_name = 'house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name = 'profile-detail')
    class Meta:
        model= TaskList
        fields =['url', 'id', 'name', 'created_on', 'created_by', 'house', 'description', 'status'  ]
        read_only_fields = ['created_on', 'status', 'notcompleted_tasks_count']