from django.db import models
from django.contrib.auth.models import User
import uuid


class TrackDateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TrackDateTime):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    duration = models.IntegerField()
    avatar = models.TextField(null=True)

    def __str__(self):
        return "{} - {} Hours".format(self.name, self.duration)


class Task(TrackDateTime):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assignee = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} - {self.project.name}"

    def get_assignees(self):
        return ",".join(self.assignee.values_list('username', flat=True))


class Subtask(TrackDateTime):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.task.name}"
