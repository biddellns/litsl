from django.contrib import admin

from .models import Season, GroupRound, Group, Matchup, Game
# Register your models here.
admin.site.register(Season)
admin.site.register(GroupRound)
admin.site.register(Group)
admin.site.register(Matchup)
admin.site.register(Game)
