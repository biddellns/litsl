from django.db import models

from django.db.models import Sum
from players.models import Player
from season.models import Group
# Create your models here.

class Matchup(models.Model):
    player1 = models.ForeignKey(Player, related_name="matchups_player1")
    player2 = models.ForeignKey(Player, related_name="matchups_player2")
    group = models.ForeignKey(Group, related_name="matchups", null=True)
    num_games = models.IntegerField() # Best of X

    # Currently making the dangerous assumption that there isn't a tie.
    def match_winner(self):
        player1_wins = self.games.aggregate(Sum('player1_score'))['player1_score__sum']
        player2_wins = self.games.aggregate(Sum('player2_score'))['player2_score__sum']

        if player1_wins > player2_wins:
            return self.player1
        else:
            return self.player2


    def __str__(self):
        return '{} Vs {}'.format(self.player1, self.player2)

class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name="games_player1")
    player2 = models.ForeignKey(Player, related_name="games_player2")
    matchup = models.ForeignKey(Matchup, related_name="games")
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()
    map_name = models.CharField(max_length = 30)
    game_number = models.IntegerField()

    def game_winner(self):
        if self.player1_score > self.player2_score:
            return self.player1
        elif self.player2_score > self.player1_score:
            return self.player2
        else:
            return None

    def __str__(self):
        return '{} Vs {} on {}'.format(self.player1, self.player2, self.map_name)
