from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksConfig(AppConfig):
    """Default app config"""

    name = "apps.api.tasks"
    verbose_name = _("Tasks")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
