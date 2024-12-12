from django.db import models


class TechniqueChoice(models.TextChoices):
    OIL_PAINTING = 'Oil Painting', 'Oil Painting'
    ACRILIC_PAINTING = 'Acrilic Painting', 'Acrilic Painting'
    WATERCOLOR_PAINTING = 'Watercolor Painting', 'Watercolor Painting'
    GOUACHE_PAINTING = 'Gouache Painting', 'Gouache Painting'
    SPRAY_PAINTING = 'Spray Painting', 'Spray Painting'
    MIXED_MEDIA = "Mixed Media", "Mixed Media"
    OTHER = "Other", "Other"
