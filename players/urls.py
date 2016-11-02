from django.conf.urls import url

from .views import PlayerList
urlpatterns = [
        url(r'^$', PlayerList.as_view()),
            
        ]
