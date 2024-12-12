from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r"^[A-Za-z0-9_]*$",
                message="Ensure this value contains only letters, numbers, and underscore"
            )],
        blank=False,
        null=False
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return self.username
