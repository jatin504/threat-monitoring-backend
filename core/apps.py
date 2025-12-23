from django.apps import AppConfig
import os


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        """
        Bootstrap admin user from environment variables.
        Runs AFTER all apps are loaded.
        """
        from django.contrib.auth import get_user_model
        from threat_platform.core.models import UserProfile

        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")
        email = os.getenv("ADMIN_EMAIL", "")

        # Env vars not set → skip
        if not username or not password:
            return

        # Admin already exists → skip
        if User.objects.filter(username=username).exists():
            return

        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )

        UserProfile.objects.create(user=user, role="ADMIN")
