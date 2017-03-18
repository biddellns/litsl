from django.conf.urls import url, include

from .views import SeasonDetail, GroupRoundDetail, ScheduleList, RulesView

urlpatterns = [
        url(r'^rules/$', RulesView.as_view(),
            name="rules"),
        url(r'^(?:(?P<pk>[0-9]+)/)?', include([
            url(r'^$', SeasonDetail.as_view(), 
                name="season_detail"),
            url(r'^(?P<group_round>[a-zA-Z]+)/$', GroupRoundDetail.as_view(),
                name="group_round_detail"),
            url(r'schedule/$', ScheduleList.as_view(),
                name="season_schedule"),
            ])),
        ]
