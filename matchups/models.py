from django.db import models

from players.models import Player
from season.models import Group
# Create your models here.

class Matchup(models.Model):
    player1 = models.ForeignKey(Player, related_name="matchups_player1")
    player2 = models.ForeignKey(Player, related_name="matchups_player2")
    group = models.ForeignKey(Group, related_name="matchups", null=True)
    num_games = models.IntegerField()

    def __str__(self):
        return '{} Vs {}'.format(self.player1, self.player2)

class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name="game_player1")
    player2 = models.ForeignKey(Player, related_name="game_player2")
    matchup = models.ForeignKey(Matchup, related_name="games")
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()
    map_name = models.CharField(max_length = 30)
    game_number = models.IntegerField()

    def __str__(self):
        return '{} Vs {} on {}'.format(self.player1, self.player2, self.map_name)
