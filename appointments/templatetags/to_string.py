from django import template

register = template.Library()

@register.filter
def to_string(value):
    return str(value)

@register.filter
def get_type(value):
    return type(value)