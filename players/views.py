from django.shortcuts import render
from django.views.generic import ListView

from .models import Player

# Create your views here.
class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'
