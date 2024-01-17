from typing import Any
from django.forms import Textarea
from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from leaderboard.views import BASE_URL_ICON
from .models import Character, Goal, Streak

# Create your views here.
class StreakingView(generic.ListView):
    model = Streak

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(approved=True)
        if 'character' in self.kwargs:
            self.character = self.kwargs['character']
            if self.character != 'all':
                query = query.filter(character__id=self.character)
        if 'goal' in self.kwargs:
            self.goal = self.kwargs['goal']
            if self.goal != 'all':
                query = query.filter(goal__id=self.goal)
        return query
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= {
            'base_url_icon': BASE_URL_ICON,
            'characters': Character.objects.all(),
            'goals': Goal.objects.all(),
            'currentcharacter': self.character,
            'currentgoal': self.goal,
        }
        return context
    

class StreakCreate(generic.CreateView):
    model = Streak
    fields = ['player', 'character', 'goal', 'score', 'alive', 
              'vod', 'game_version', 'ebsi', 'optional_comment']
    success_url = '/streaking/all/all/'
    initial = {
        'game_version': '1.7.9b',
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.required_css_class = 'required'
        form.fields['player'].label = 'Twitch name'
        form.fields['vod'].label = 'Link to a Twitch clip/broadcast'
        form.fields['character'].queryset = Character.objects.exclude(id='all')
        form.fields['goal'].queryset = Goal.objects.exclude(id='all')
        form.fields['optional_comment'].widget = Textarea(attrs={"cols":30, "rows":2})
        for f in form.fields:
            form.fields[f].label_suffix = ''
        return form