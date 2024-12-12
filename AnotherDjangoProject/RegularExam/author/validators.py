from django.core.exceptions import ValidationError


def name_validator(value):
    if not value.isalpha():
        raise ValidationError('Your name must contain letters only!')


def password_validator(value):
    if not len(value) == 6:
        raise ValidationError('Your passcode must be exactly 6 digits!')
