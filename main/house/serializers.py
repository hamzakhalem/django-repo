from rest_framework import serializers
from .models import House
class HouseSerializers(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only=True)

    class Meta:
        model= House
        fields =['url', 'id', 'user', 'created_on', 'manager', 'description', 'points', 'completed_tasks_count', 'notcompleted_tasks_count' ]
        read_only_fields = ['points', 'completed_tasks_count', 'notcompleted_tasks_count']