from django.db import models
import uuid
from django.utils.deconstruct import deconstructible
import os 

@deconstructible
class GenerateProfileImagePath(object):
    
    def __init__(self):
        pass
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'media/houses/{instance.id}/images'
        name = f'main.{ext}'
        return os.path.join(path, name)

houseImagePath = GenerateProfileImagePath()
# Create your models here.
class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=120)
    image = models.FileField( upload_to=houseImagePath, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    manager = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_house')
    points = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    notcompleted_tasks_count = models.IntegerField(default=0)
