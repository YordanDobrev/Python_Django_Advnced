from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class ArtoniaUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="artonia_user",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="artonia_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )
