from django import template
from tasty_recypes.utils import get_user_obj

register = template.Library()


@register.simple_tag
def user_profile():
    return get_user_obj()