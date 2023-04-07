from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiplies the value and the argument
    """
    return value * arg
