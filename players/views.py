from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import FormView, TemplateView

from .models import Player
from .forms import PlayerForm

# Create your views here.
class HomePage(TemplateView):
    template_name = 'players/index.html'

class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'
    context_object_name = 'players'

class PlayerDetail(DetailView):
    model = Player
    #template_name = 'player_detail.html'
    context_object_name = 'player'

class SignUpForm(FormView):
    template_name = 'players/signup.html'
    form_class = PlayerForm
    success_url = '/'
