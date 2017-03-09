from allauth.socialaccount.providers.battlenet.provider import BattleNetProvider

class BattleNetSC2ScopeProvider(BattleNetProvider):
    id = 'battlenet_sc2scope'

    def get_default_scope(self):
        return "sc2.profile"
