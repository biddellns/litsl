from django import template

register = template.Library()

@register.filter
def access(dictionary, key):
    return dictionary[key]

@register.simple_tag
def group_matchup_record(player, group):
    return player.get_matchup_record(group)

@register.simple_tag
def group_game_record(player, group):
    return player.get_game_record(group)

@register.simple_tag
def record_print(record_dict):
    wins = record_dict["wins"]
    losses = record_dict["losses"]
    return "{} - {}".format(wins, losses)
    
