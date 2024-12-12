from django.core.exceptions import ValidationError


def validate_photos(image_object):
    if image_object.size >= 5 * 1024 * 1024:
        raise ValidationError("The maximum allowed size is 5MB")
