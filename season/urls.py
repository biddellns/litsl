from django.conf.urls import url

from .views import SeasonDetail, ScheduleList
urlpatterns = [
        url(r'^$', SeasonDetail.as_view(), 
            name='season_detail_default'),
        url(r'^(?:(?P<pk>[0-9]+))?/$', SeasonDetail.as_view(),
            name='season_detail'),
        url(r'^(?P<season>[0-9]+)/schedule/$', ScheduleList.as_view(),
            name="season_schedule"),
        url(r'^schedule/$', ScheduleList.as_view(),
            name="season_schedule_default"),
#        url(r'^(?P<pk>[0-9]+)/$', PlayerDetail.as_view(), name='player_detail'),            
        ]
