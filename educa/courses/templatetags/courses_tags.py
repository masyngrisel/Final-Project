from django import template
from ..models import Course

register = template.Library()

@register.simple_tag
def total_courses():
    return Course.published.count()