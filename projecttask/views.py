from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, redirect

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Project, Task, Subtask
from api.serializers.project import ProjectSerializer
from api.serializers.task import TaskSerializer
from api.serializers.subtask import SubTaskSerializer


class ProjectsListView(TemplateView):

    template_name = "project/home.html"


class ProjectsAddView(TemplateView):

    template_name = "project/add-project.html"


class ProjectsEditView(TemplateView):

    template_name = "project/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = kwargs.get('project_id')
        return context


class ProjectsDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "project/detail.html"

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        tasks = Task.objects.all()
        return Response({"project": project, "tasks": tasks})


class TaskAddEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/add_new.html'

    def get(self, request, pk=None, project_id=None):
        if pk and pk != "create" and project_id != "create":
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task)
        else:
            task = None
            serializer = TaskSerializer(context={'request': request})

        json_response = {
            'serializer': serializer,
            'task': task,
            "pk": pk,
            "project_id": project_id,
            "action_type": "Create New"
        }
        return Response(json_response)

    def post(self, request, pk=None, project_id=None):
        if pk and pk != "create" and project_id != "create":
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task, data=request.data)
        else:
            task = None
            serializer = TaskSerializer(data=request.data)

        if not serializer.is_valid():
            json_response = {
                'serializer': serializer,
                'task': task,
                "pk": pk,
                "project_id": project_id,
                "action_type": "Update"
            }
            return Response(json_response)

        instance = serializer.save()
        return redirect('project-detail-view', project_id=instance.project.pk)


class TaskDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "task/detail.html"

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        subtasks = Subtask.objects.all()
        return Response({"task": task, "subtasks": subtasks})


class SubTaskAddEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subtask/add_new.html'

    def get(self, request, pk=None, project_id=None, subtask_id=None):
        if pk and pk != "create" and project_id != "create" \
         and subtask_id != "create":
            subtask = get_object_or_404(Subtask, pk=subtask_id)
            serializer = SubTaskSerializer(subtask)
        else:
            subtask = None
            serializer = SubTaskSerializer(context={'request': request})

        json_response = {
            'serializer': serializer,
            'subtask': subtask,
            "pk": pk,
            "project_id": project_id,
            "subtask_id": subtask_id,
            "action_type": "Create New"
        }
        return Response(json_response)

    def post(self, request, pk=None, project_id=None, subtask_id=None):
        if pk and pk != "create" and project_id != "create" \
         and subtask_id != "create":
            subtask = get_object_or_404(Subtask, pk=subtask_id)
            serializer = SubTaskSerializer(subtask, data=request.data)
        else:
            subtask = None
            serializer = SubTaskSerializer(data=request.data)

        if not serializer.is_valid():
            json_response = {
                'serializer': serializer,
                'subtask': subtask,
                "pk": pk,
                "project_id": project_id,
                "action_type": "Update"
            }
            return Response(json_response)

        instance = serializer.save()
        return redirect('task-detail-view', task_id=instance.task.pk)
