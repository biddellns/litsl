from django import forms

from season.models import Group,GroupRound, Season

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        exclude = [ ]
