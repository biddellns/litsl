from django.test import TestCase

from django.core.urlresolvers import resolve

import players
#from players.views import PlayerList
# Create your tests here.

class PlayerListPageTest(TestCase):
    def test_root_slash_players_resolves_to_player_list_view(self):
        found = resolve('/players/')
        self.assertEqual(found.view_name, 'players.views.PlayerList')
