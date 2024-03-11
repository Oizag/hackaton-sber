from rest_framework import serializers
from apps.api.company.models import (
  Project,
  Task
  )

class ProjectAPI(serializers.ModelSerializer):

    class Meta:
      model = Project
      fields = "__all__"

class ProjectTasksAPI(serializers.ModelSerializer):

    class Meta:
      model = Task
      fields = "__all__"

