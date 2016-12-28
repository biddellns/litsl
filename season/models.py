from django.db import models
from django.db.models import Sum
from django.contrib import admin

from players.models import Player

# Create your models here.
class Season(models.Model):
   season_number = models.AutoField(primary_key=True)

   def __str__(self):
       return "Season {}".format(self.season_number)
   
class GroupRound(models.Model):
    season = models.ForeignKey(Season, related_name="group_rounds")
    num_players = models.IntegerField()

    def __str__(self):
        return "Round of {}".format(self.num_players)

class Group(models.Model):
    group_name = models.CharField(max_length=10)
    group_round = models.ForeignKey(GroupRound, related_name="groups")
    players = models.ManyToManyField(Player)
    schedule_is_set = models.BooleanField(default=False)

    def create_group_schedule(self):
        if not self.schedule_is_set:
            players = self.players.all()

            for i in range(len(players)):
                for j in range(i + 1, len(players)):
                    Matchup(
                            player1 = players[i], 
                            player2 = players[j], 
                            group = self, 
                            num_games=3
                            ).save()
                    
                    # Hack to get the recently saved MU.
                    mu = Matchup.objects.last()

                    # Create the games making up the 'Best of X'.
                    mu.create_game_sets()

            self.schedule_is_set = True
            self.save()
            return True
        else:
            return False
    
    def delete_group_schedule(self):
        if self.schedule_is_set:
            for mu in self.matchups.iterator():
                mu.delete()
            self.schedule_is_set = False
            self.save()
            return True
        else:
            return False
            

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ['group_name']

class Matchup(models.Model):
    player1 = models.ForeignKey(Player, related_name="matchups_player1")
    player2 = models.ForeignKey(Player, related_name="matchups_player2")
    group = models.ForeignKey(Group, related_name="matchups", null=True)
    num_games = models.IntegerField() # Best of X

    # Currently making the dangerous assumption that all games will be recorded.
    def match_winner(self):
        player1_wins = self.games.aggregate(Sum('player1_score'))['player1_score__sum'] or 0
        player2_wins = self.games.aggregate(Sum('player2_score'))['player2_score__sum'] or 0

        if player1_wins > player2_wins:
            return self.player1
        elif player2_wins > player1_wins:
            return self.player2
        else:
            return None

    # Create games based on how many are specified in the num_games field.
    def create_game_sets(self):
        for i in range(1, self.num_games + 1):
            self.games.create(
            player1 = self.player1,
            player2 = self.player2,
            game_number = i
            )


    def __str__(self):
        return '{} Vs {}'.format(self.player1, self.player2)

class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name="games_player1")
    player2 = models.ForeignKey(Player, related_name="games_player2")
    matchup = models.ForeignKey(Matchup, related_name="games")
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    map_name = models.CharField(max_length = 30, null=True, default="TBD")
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
