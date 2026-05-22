from django.urls import path, include

from rest_framework_nested import routers

from .viewsets.project import ProjectViewSet
from .viewsets.task import TaskViewSet
from .viewsets.subtask import SubTaskViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = routers.NestedSimpleRouter(router,
                                             r'projects',
                                             lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename='task')

router.register(r'subtasks', SubTaskViewSet, basename='subtask')

urlpatterns = [
                path('', include(router.urls)),
                path('', include(projects_router.urls))
]
