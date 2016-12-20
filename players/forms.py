from django import forms

from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['bnet_name', 'bnet_id', 'bnet_profile_url', 'discord_name', 'race', 'league' ]
