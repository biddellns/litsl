import requests, json

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .models import Player

class MyPlayerAdapter(DefaultSocialAccountAdapter):

        def get_1v1_games_count(self, season_stats):
                for ladder in season_stats:
                        if ladder['type'] == '1v1':
                                return ladder['games']

                return 0

        """
        After an intial user is saved (validated), populate a Player object
        and link it to the newly created user.
        """
        def save_user(self, request, sociallogin, form = None):
                user = super().save_user(request, sociallogin, form)

                # Build URL to access user data

                # Base URL
                url = "https://us.api.battle.net/sc2/profile/user?"

                # User will have only one blizzard account and therefore only one token
                socialtoken = user.socialaccount_set.first().socialtoken_set.first()

                params = dict(
                        access_token = socialtoken,
                        )

                # Make call for user data
                user_json_data = requests.post(url=url, params=params).json()

                # Grab the first character we see
                sc2_profile = user_json_data['characters'][0]

                sc2_name = sc2_profile['name']
                team = sc2_profile['clanName'] or " "


                ladder_stats = sc2_profile['season']['stats']
                ladder_games_played = self.get_1v1_games_count(ladder_stats)

                # Grab first letter for db
                league = sc2_profile['career']['highest1v1Rank'] # Get the highest 1v1 league ever.
                league = league[0]

                player = Player.objects.create(user=user, sc2_name=sc2_name, team=team, league=league, ladder_games_played = ladder_games_played)
                player.save()

