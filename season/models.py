from django.db import models

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

    def __str__(self):
        return self.group_name
