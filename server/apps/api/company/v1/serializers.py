from rest_framework import serializers
from apps.api.company.models import Project

# Create your serializers here.
class Meta:
        model = Project
        fields = ("name", "slug", "cost",  "last_modify_user", "last_modify_date", "progress", "start_date", "deadline_date", "status")