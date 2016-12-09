from django.contrib import admin
from django import forms

from .forms import GroupForm
from .models import Season, GroupRound, Group, Matchup, Game


class GroupAdmin(admin.ModelAdmin):
    actions = ['generate_schedule', 'delete_schedule']

    def generate_schedule(modeladmin, request, queryset):
        for group in queryset:
            group.create_group_schedule()
            short_description = "Generate round-robin schedule for selected groups"
    
    def delete_schedule(modeladmin, request, queryset):
        for group in queryset:
            group.delete_group_schedule()
            short_description = "Delete schedule for selected groups"

admin.site.register(Season)
admin.site.register(GroupRound)
admin.site.register(Group, GroupAdmin)
admin.site.register(Matchup)
admin.site.register(Game)
