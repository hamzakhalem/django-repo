from django.db import models
import uuid
from django.utils.deconstruct import deconstructible
import os 


NOT_COMPLETED = 'NC'
COMPLETED = 'C'
# Create your models here.
TASK_STATUS_CHOICEs = [
    (NOT_COMPLETED, 'not completed'),
    (COMPLETED, 'completed'),
] 

@deconstructible
class GenerateAttachmentsFilePath(object):
        
    def __init__(self):
        pass
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'media/tasks/{instance.task.id}/files'
        name = f'{instance.id}.{ext}'
        return os.path.join(path, name)

generateAttachmentsFilePath = GenerateAttachmentsFilePath()
class TaskList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    created_by = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='Lists')
    house = models.ForeignKey("house.House", on_delete=models.CASCADE,  related_name='Lists')   
    name = models.CharField( max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField( max_length=50, choices= TASK_STATUS_CHOICEs, default=NOT_COMPLETED)
    def __str__(self):
        return self.name


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    created_by = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='created_tasks')
    completed_by = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='completed_tasks')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField( max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField( max_length=50, choices= TASK_STATUS_CHOICEs, default=NOT_COMPLETED)

    def __str__(self):
        return self.name
    
class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to=generateAttachmentsFilePath)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,  related_name='atachements') 

    def __str__(self):
        return f'{self.id} | {self.task}'