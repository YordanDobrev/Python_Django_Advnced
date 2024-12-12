from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pets
from Petstagram.photos.validators import validate_photos


# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='media/',
        validators=(validate_photos,)
    )

    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
    )

    location = models.CharField(
        max_length=30,
    )

    tagged_pets = models.ManyToManyField(
        to=Pets,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )
