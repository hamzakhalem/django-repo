from django.db.models.signals import  post_save, pre_save
from django.dispatch import receiver
from .models import TaskList, Attachment, Task, COMPlETE, NOT_COMPLETE

@receiver(post_save, sender=Task)
def update_house_points(sender, instance, created, **kwargs):
    house = instanse.task.list_house
    if instance.status == COMPLETE:
        house.points += 10
    elif instance.status == NOT_COMPLETE:
        if(house.points >= 10):
            house.points -= 10
    house.save()

@receiver(post_save, sender=TaskList)
def update_tasklist_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_complete = True
    for task in task_list.task.all():
        if task.status != COMPLETE:
            is_complete = False
            break
    if(is_complete)
        task_list.status = COMPlETE
    else
        task_list.status = NOT_COMPlETE
    task_list.save()
