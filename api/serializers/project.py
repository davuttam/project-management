from rest_framework import serializers

from django.urls import reverse

from projecttask.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "description", "duration", "detail_url"]

    def get_detail_url(self, obj):
        return reverse('project-edit-view', kwargs={'project_id': str(obj.pk)})
