from rest_framework import serializers
from apps.api.company.models import Project


# Create your serializers here.
class Meta:
    model = Project
    fields = "__all__"