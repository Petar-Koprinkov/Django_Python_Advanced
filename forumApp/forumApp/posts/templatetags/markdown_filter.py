from django import template

from markdown import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    return markdown(text)