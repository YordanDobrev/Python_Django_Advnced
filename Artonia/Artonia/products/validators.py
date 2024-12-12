from django.core.exceptions import ValidationError


def bad_words(value):
    BAD_WORDS = ["Worse", "Ugly"]

    for word in BAD_WORDS:
        if word.lower() in value.lower():
            raise ValidationError(f"'{word}' is a BAD word and it is not valid.")