from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "core"
    verbose_name = _("app__core")


__all__ = []
