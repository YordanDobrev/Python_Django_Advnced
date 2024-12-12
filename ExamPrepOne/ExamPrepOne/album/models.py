from django.core.validators import MinValueValidator
from django.db import models

from ExamPrepOne.account.models import Profile


# Create your models here.
class Album(models.Model):
    MUSIC_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    genre = models.CharField(
        max_length=30,
        choices=MUSIC_CHOICES,
        default='Other',
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='albums',
    )
