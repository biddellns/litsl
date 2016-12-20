from django.conf.urls import url

from .views import PlayerList, PlayerDetail, SignUpForm
urlpatterns = [
        url(r'^$', PlayerList.as_view(),
            name='player_list'),
        url(r'signup/$', SignUpForm.as_view(),
            name="signup"),
        url(r'^(?P<pk>[0-9]+)/$', PlayerDetail.as_view(), name='player_detail'),            
        ]
