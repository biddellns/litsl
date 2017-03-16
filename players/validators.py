from allauth import socialaccount

def username_validators():
    return [
            socialaccount.providers.battlenet.validators.BattletagUsernameValidator,
           ]
