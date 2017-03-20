from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .models import Player

class MyPlayerAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social login provider but before the login is actually processed
        (and before the pre_social_login signal is emitted).

        We're trying to solve for two use cases:
        - social account already exists: Keep going through flow.
        - social account is new: Create new player model and link it.
        """

        # Ignore existing social accounts. They should already be linked to
        # a player model.
        # 
        # Else, create a new player object.
        if sociallogin.is_existing:
            return
        else:
            player = Player.objects.create()
