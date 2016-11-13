from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Matchup, Game

# Create your views here.
class MatchupList(ListView):
    model = Matchup
    template_name = 'matchup_list.html'
    context_object_name = 'matchups'

class MatchupDetail(DetailView):
    model = Matchup
    template_name = 'matchups/matchup_detail.html'
    context_object_name = 'matchup'

class GameList(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'

class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'
