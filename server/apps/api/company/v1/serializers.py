from rest_framework import serializers
from apps.core.utils.fields import TextChoiceField
from apps.api.company.models import (
  Project,
  Task
  )

# Вот это для игоря пусть посмотрит как это делается
class ProjectAPI(serializers.ModelSerializer):
	perspective = TextChoiceField(choices=Project.Perspective.choices, read_only=True)
	status = TextChoiceField(choices=Project.Status.choices, read_only=True)
	class Meta:
		model = Project
		fields = "__all__"

class ProjectTasksAPI(serializers.ModelSerializer):

    class Meta:
      model = Task
      fields = "__all__"

