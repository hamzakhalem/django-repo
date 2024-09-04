from django.db import models

NOT_COMPLETED = 'NC'
COMPLETED = 'C'
# Create your models here.
TASK_STATUS_CHOICEs = [
    (NOT_COMPLETED, 'not completed'),
    (COMPLETED, 'completed'),
] 

class House(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    created_by = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='created_tasks')
    completed_by = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='completed_tasks')
    name = models.CharField( max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField( max_length=50, choices= TASK_STATUS_CHOICEs, default=NOT_COMPLETED)

    def __str__(self):
        return self.name
