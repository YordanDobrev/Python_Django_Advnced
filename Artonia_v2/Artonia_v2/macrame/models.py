from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.common.models import Product, Like
from Artonia_v2.macrame.choices import KnotChoices


class Macrame(Product):
    user = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE,
    )

    knot_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    difficulty_level = models.CharField(
        max_length=20,
        choices=KnotChoices.choices,
        default="Beginner"
    )

    is_public = models.BooleanField(
        default=False
    )

    last_bid = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=True,
        null=True,
    )

    bidder = models.CharField(
        blank=True,
        null=True,
    )

    bid_due_date = models.DateField()

    likes = GenericRelation(Like)

    def total_likes(self):
        return self.likes.count()
