from django.conf.urls import url

from .views import PlayerList, PlayerDetail
urlpatterns = [
        url(r'^$', PlayerList.as_view(),
            name='player_list'),
        url(r'^(?P<pk>[0-9]+)/$', PlayerDetail.as_view(), name='player_detail'),            
        ]
