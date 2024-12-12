from django.core.validators import MinLengthValidator
from django.db import models

from RegularExam.author.validators import name_validator, password_validator


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4), name_validator],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), name_validator],
    )

    passcode = models.CharField(
        max_length=6,
        validators=[password_validator],
        help_text="Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )
