from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message='Username must be at least 3 chars long!'),
            RegexValidator(
                regex=r"^[A-Za-z0-9_]*$",
                message="Username must contain only letters, digits, and underscores!"
            )
        ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(21, message='Age requirement: 21 years and above.')],
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

