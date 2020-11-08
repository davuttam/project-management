from django.urls import path

from .views import (
    ProjectsAddView,
    ProjectsEditView,
    ProjectsDetail,
    TaskAddEdit,
    TaskDetail,
    SubTaskAddEdit
)

urlpatterns = [
    path('add', ProjectsAddView.as_view(), name='project-add-view'),
    path('edit/<str:project_id>', ProjectsEditView.as_view(), name='project-edit-view'),
    path('detail/<str:project_id>', ProjectsDetail.as_view(), name='project-detail-view'),
    path(
        '<project_id>/task-add-edit/<pk>',
        TaskAddEdit.as_view(),
        name='task-add-edit'
    ),
    path(
        '<project_id>/task-add-edit/<pk>/subtask/<subtask_id>',
        SubTaskAddEdit.as_view(),
        name='subtask-add-edit'
    ),
    path('task/detail/<str:task_id>', TaskDetail.as_view(), name='task-detail-view'),
]
