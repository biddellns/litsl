from django.contrib import admin, messages
from django import forms

from .forms import GroupForm
from .models import Season, GroupRound, Group, Matchup, Game


class GroupAdmin(admin.ModelAdmin):
    actions = ['generate_schedule', 'delete_schedule']

    def change_view(self, request, object_id, form_url='', extra_context = None):
        extra_context = extra_context or {}
        

        return super(GroupAdmin, self).change_view(
                request, object_id, form_url,
                extra_context = extra_context)
        

    def generate_schedule(self, request, queryset):
        created_groups = []
        for group in queryset:
            if group.create_group_schedule():
                created_groups.append(group.group_name)
 
        message = ""
        level = messages.SUCCESS
        if len(created_groups) == 0:
            message = "No schedules were generated for the selected groups."
            level = messages.ERROR
        else:
            message = "Schedules were generated for {}".format(created_groups)

        self.message_user(request, message, level)
        self.short_description = "Generate round-robin schedule for selected groups"

    def delete_schedule(self, request, queryset):
        deleted_groups = []
        for group in queryset:
            if group.delete_group_schedule():
                deleted_groups.append(group.group_name)

        message = ""
        level = messages.SUCCESS
        if len(deleted_groups) == 0:
            message = "No schedules were deleted for the selected groups."
            level = messages.ERROR
        else:
            message = "Schedules were deleted for {}".format(deleted_groups)

        self.message_user(request, message, level)
        self.short_description = "Delete schedule for selected groups"

admin.site.register(Season)
admin.site.register(GroupRound)
admin.site.register(Group, GroupAdmin)
admin.site.register(Matchup)
admin.site.register(Game)
