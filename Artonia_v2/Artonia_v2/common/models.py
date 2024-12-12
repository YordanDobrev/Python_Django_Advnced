from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Like(models.Model):
    """
    A generic Like model that can be used with multiple content types
    """
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    # Content type of the liked object
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE
    )

    # Object ID of the liked object
    object_id = models.PositiveIntegerField()

    # Generic foreign key to the liked object
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate likes
        unique_together = ('user', 'content_type', 'object_id')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} liked {self.content_object}"
