from django.db import models


class KnotChoices(models.TextChoices):
    BEGINNER = "Beginner", "Beginner"
    INTERMEDIATE = "Intermediate", "Intermediate"
    ADVANCED = "Advanced", "Advanced"
