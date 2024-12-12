from django import template

from music_app_exam_prep.utils import get_user_obj

register = template.Library()


@register.simple_tag
def get_user():
    return get_user_obj()
