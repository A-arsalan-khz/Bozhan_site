from django import template

register = template.Library()

@register.filter
def binary_to_int(value):
    try:
        return int(value, 2)  # Convert binary (e.g., '0110') to integer
    except (ValueError, TypeError):
        return value
