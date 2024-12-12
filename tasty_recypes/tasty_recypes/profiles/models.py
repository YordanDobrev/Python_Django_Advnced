from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from tasty_recypes.profiles.validators import validate_first_name


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(2, message="Nickname must be at least 2 chars long!")],
    )

    first_name = models.CharField(
        max_length=30,
        validators=[validate_first_name]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[validate_first_name]
    )

    chef = models.BooleanField(
        default=False,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

