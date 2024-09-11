from rest_framework import routers
from .viewsets import TaskListViewSet, TasktViewSet, AttachmenttViewSet

app_name = "tasklist"

router = routers.DefaultRouter()
router.register("tasklists", TaskListViewSet)
router.register("tasks", TasktViewSet)
router.register("attachments", AttachmenttViewSet)
