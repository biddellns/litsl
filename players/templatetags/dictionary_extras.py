from django import template

register = template.Library()

@register.filter(name='access')
def access(dictionary, key):
    return dictionary[key]
