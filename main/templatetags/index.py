from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    if len(indexable) > i:
        return indexable[i]
    return None

@register.filter
def mul(value, arg):
    return value * arg
