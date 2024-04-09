from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = gettext_lazy("app__users")


__all__: list[str] = []
