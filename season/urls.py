from django.conf.urls import url, include

from .views import SeasonDetail, ScheduleList, RulesView
urlpatterns = [
        url(r'^(?:(?P<pk>[0-9]+)/)?', include([
            url(r'^$', SeasonDetail.as_view(), 
                name="season_detail"),
            url(r'schedule/$', ScheduleList.as_view(),
                name="season_schedule"),
            url(r'^rules/$', RulesView.as_view(),
                name="rules"),
            ])),
        ]
