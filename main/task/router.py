from rest_framework import routers
from .viewsets import TaskListViewSet

app_name = "tasklist"

router = routers.DefaultRouter()
router.register("taskLlists", TaskListViewSet)
