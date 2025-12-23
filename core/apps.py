import os
from django.contrib.auth.models import User
from django.apps import AppConfig
from threat_platform.core.models import UserProfile


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")
        email = os.getenv("ADMIN_EMAIL", "")

        if not username or not password:
            return

        if User.objects.filter(username=username).exists():
            return

        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )

        UserProfile.objects.create(user=user, role="ADMIN")
