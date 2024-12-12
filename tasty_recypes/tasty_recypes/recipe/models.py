from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tasty_recypes.profiles.models import Profile
from tasty_recypes.recipe.choices import RecipeChoices


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(10)],
        error_messages={'unique': 'We already have a recipe with the same title!'},
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=RecipeChoices.choices
    )

    ingredients = models.TextField()

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes."
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
