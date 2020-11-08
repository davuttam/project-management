from rest_framework import serializers

from projecttask.models import Task

from .project import ProjectSerializer


class TaskSerializer(serializers.ModelSerializer):
    # project = ProjectSerializer()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
            "project",
            "assignee"
        ]
