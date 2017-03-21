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
    bnet_profile_url = models.URLField("Battle.net Profile URL",
            validators = [
                    RegexValidator(
                        regex='^(http(s)?:\/\/)?(eu|us|kr)\.battle.net\/sc2\/(en)\/profile\/\d{6,7}\/\d\/\w+\/$',
                        message="This doesn't appear to be a valid profile link.",
                        code='Invalid URL'
                        ),
                ],
                null = True
            )
    discord_name = models.CharField("Discord Username", max_length = 30, null = True)
    sc2_name = models.CharField(max_length = 30, null = True)
    league = models.CharField(max_length = 1, choices = LEAGUE_LEVELS)
    race = models.CharField(max_length = 1, choices = RACES, null = True)
    ladder_games_played = models.IntegerField(blank = True, null = True)
    team = models.CharField(max_length = 30)

    def get_total_games(self, *args):
        record = self.get_game_record(args)
        return record['wins'] + record['losses']


    def get_wins(self, *args):
        return self.get_game_record(args)['wins']

    def get_losses(self, *args):
        return self.get_game_record(args)['losses']

    def get_matchup_record(self, *args):
        wins = 0
        losses = 0
        
        if not args or args[0] == (): # If a group wasn't specified, return a value of -1.
            _group = -1 
        else:
            _group = args[0].pk 

        if _group == -1:
            matchups = self.matchups_player1.all() | self.matchups_player2.all()
        else:
            # If a group was specified, find all the matchups in the group where this player played in.
            matchups = self.matchups_player1.filter(group = _group) | self.matchups_player2.filter(group=_group)
       
        for match in matchups:
            winner = match.match_winner()
            if winner is not None: # If the match isn't completed.
                if winner == self:
                    wins += 1
                else:
                    losses += 1

        record = {
                'wins': wins,
                'losses': losses,
                }

        return record
    
    def get_game_record(self, *args):
        wins = 0
        losses = 0
        games = []

        if not args or args[0] == (): # If a group wasn't specified, return a value of -1.
            _group = -1 
        else:
            _group = args[0].pk 

        if _group == -1:
            matchups = self.matchups_player1.all()  | self.matchups_player2.all()
        else:
            # If a group was specified, find all the matchups in the group where this player played in. Used to find all related games.
            matchups = self.matchups_player1.filter(group = _group) | self.matchups_player2.filter(group = _group)

        # Create the set of games from the list of matchups.
        for matchup in matchups:
            for game in matchup.games.all():
                games.append(game)

        for game in games:
            winner = game.game_winner()
            if winner is not None:
                if winner == self:
                    wins += 1
                else:
                    losses += 1

        record = {
                'wins': wins,
                'losses': losses
                }

        return record

    def __str__(self):
        return '{}'.format(self.sc2_name)
