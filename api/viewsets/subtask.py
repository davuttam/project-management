from rest_framework import mixins, generics
from rest_framework import viewsets

from projecttask.models import Subtask
from api.serializers.subtask import SubTaskSerializer


class SubTaskViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = []
