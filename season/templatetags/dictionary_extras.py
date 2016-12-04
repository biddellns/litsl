from django import template

register = template.Library()

@register.filter
def access(dictionary, key):
    return dictionary[key]

@register.simple_tag
def record_print(record_dict):
    wins = record_dict["wins"]
    losses = record_dict["losses"]
    return "{} - {}".format(wins, losses)
    
