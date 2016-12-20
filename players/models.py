from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

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

    bnet_name = models.CharField("Battle.net Username", max_length = 30)
    bnet_id = models.IntegerField("Battle.net ID")
    bnet_profile_url = models.URLField("Battle.net Profile URL",
            validators = [
                    RegexValidator(
                        regex='(http(s)?:\/\/)?[eu|na|kr]\.battle.net\/sc2\/(en)\/profile\/\d{6,7}\/\d\/\w+\/$',
                        message='This doesn\'t appear to be a valid profile link.'
                        ),
                ]
            )
    discord_name = models.CharField("Discord Username", max_length = 30)
    sc2_name = models.CharField(max_length = 30, null = True)
    sc2_id = models.IntegerField(null = True)
    league = models.CharField(max_length = 1, choices = LEAGUE_LEVELS)
    race = models.CharField(max_length = 1, choices = RACES)
    ladder_games_played = models.IntegerField(blank = True, null = True)
    team = models.CharField(max_length = 30)

    def get_total_matches(self):
        total_matches = self.matchups_player1.count() + self.matchups_player2.count()
        
        return total_matches

    def get_total_games(self):
        total_games = self.games_player1.count() + self.games_player2.count()

        return total_games

    def get_matchup_record(self):
        wins = 0
        losses = 0
        
        for match in self.matchups_player1.iterator():
            winner = match.match_winner()
            if winner is not None: # If the match isn't completed.
                if winner is self:
                    wins += 1
                else:
                    losses += 1

        for match in self.matchups_player2.iterator():
            winner = match.match_winner()

            if winner is not None: # If the match isn't completed.
                if match.match_winner() is self:
                    wins += 1
                else:
                    losses += 1

        record = {
                'wins': wins,
                'losses': losses,
                }

        return record

    def get_game_record(self):
        wins = 0
        losses = 0

        for game in self.games_player1.all():
            if game.game_winner() is not None:
                if game.game_winner() is self:
                    wins += 1
                else:
                    losses += 1
        
        for game in self.games_player2.all():
            if game.game_winner() is not None:
                if game.game_winner() is self:
                    wins += 1
                else:
                    losses += 1
        record = {
                'wins': wins,
                'losses': losses
                }
        return record

    def __str__(self):
        return '{}#{}'.format(self.bnet_name, self.bnet_id)
