from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmployeesConfig(AppConfig):
    """Default app config"""

    name = "apps.api.employees"
    verbose_name = _("Employees")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
