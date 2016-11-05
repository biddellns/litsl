from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Player

# Create your views here.
class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'
    context_object_name = 'players'

class PlayerDetail(DetailView):
    model = Player
    #template_name = 'player_detail.html'
    context_object_name = 'player'
