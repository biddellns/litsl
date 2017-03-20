import requests, json

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .models import Player

class MyPlayerAdapter(DefaultSocialAccountAdapter):

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
        
        # Grab first letter for db
        ladder_games_played = sc2_profile['season']['totalGamesThisSeason'][:1]
        
        league = sc2_profile['career']['highest1v1Rank'] # Get the highest 1v1 league ever.

        player = Player.objects.create(user=user, sc2_name=sc2_name, team=team)
        player.save()

