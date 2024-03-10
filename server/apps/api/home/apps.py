from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    """Default app config"""

    name = "apps.api.home"
    verbose_name = _("Home")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
