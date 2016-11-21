from django.conf.urls import url

from .views import MatchupList, MatchupDetail
from .views import GameList, GameDetail

urlpatterns = [
        url(r'^$', MatchupList.as_view(),
            name='matchup_list'),
        url(r'^(?P<pk>[0-9]+)/$', MatchupDetail.as_view(),
            name='matchup_detail'),            
        url(r'^games/$', GameList.as_view(),
            name='game_list'),
        url(r'^games/(?P<pk>[0-9]+)/$', GameDetail.as_view(),
            name='game_detail'),            
        ]
