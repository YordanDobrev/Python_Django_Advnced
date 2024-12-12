from django.core.validators import MinValueValidator
from django.db import models

from music_app_exam_prep.album.choices import GenreChoices
from music_app_exam_prep.profiles.models import Profile


# Create your models here.

class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[MinValueValidator(0.1)],
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='albums',
    )