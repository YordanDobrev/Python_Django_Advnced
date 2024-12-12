from django import template

register = template.Library()

@register.filter
def split(value, delimiter=', '):
    """
    Splits the input string by the given delimiter and returns a list.
    Usage in template: {{ value|split:", " }}
    """
    if isinstance(value, str):
        return value.split(delimiter)
    return []
