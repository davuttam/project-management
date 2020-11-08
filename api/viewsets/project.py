from rest_framework import mixins, generics
from rest_framework import viewsets

from projecttask.models import Project
from api.serializers.project import ProjectSerializer


class ProjectViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []
