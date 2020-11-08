from django.contrib import admin
from projecttask.models import Project, Task, Subtask


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Subtask)
