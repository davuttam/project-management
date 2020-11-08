from rest_framework import serializers

from projecttask.models import Subtask

from .task import TaskSerializer


class SubTaskSerializer(serializers.ModelSerializer):
    # task = TaskSerializer()

    class Meta:
        model = Subtask
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
            "task"
        ]
