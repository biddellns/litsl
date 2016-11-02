from django.db import models
from django.conf import settings

# Create your models here.
LEAGUE_LEVELS = (
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
        ('D', 'Diamond'),
        ('M', 'Masters'),
        )

RACES = (
    ('P', 'Protoss'),
    ('T', 'Terran'),
    ('Z', 'Zerg'),
    ('R', 'Random'),
    )

class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank = True, null = True) # Connects a site SC2 profile to a Django User object.

    bnet_name = models.CharField(max_length = 30)
    bnet_id = models.IntegerField()
    bnet_profile_url = models.URLField()
    sc2_name = models.CharField(max_length = 30)
    sc2_id = models.IntegerField()
    league = models.CharField(max_length = 1, choices = LEAGUE_LEVELS)
    race = models.CharField(max_length = 1, choices = RACES)
    ladder_games_played = models.IntegerField(blank = True, null = True)
    team = models.CharField(max_length = 30)

    
