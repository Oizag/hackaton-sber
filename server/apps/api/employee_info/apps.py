from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmployeeInfoConfig(AppConfig):
    """Default app config"""

    name = "apps.api.employee_info"
    verbose_name = _("EmployeeInfo")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
