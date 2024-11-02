from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag(name='current_time')
def current_time(format_time='%d/%m/%y %H:%M:%S'):
    return datetime.now().strftime(format_time)