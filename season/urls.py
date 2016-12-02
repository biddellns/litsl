from django.conf.urls import url

from .views import SeasonDetail
urlpatterns = [
        url(r'^$', SeasonDetail.as_view(),
            name='season_detail'),
#        url(r'^(?P<pk>[0-9]+)/$', PlayerDetail.as_view(), name='player_detail'),            
        ]
