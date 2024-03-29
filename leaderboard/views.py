from ipware import get_client_ip
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Item, Match, Vote

BASE_URL_ICON = 'https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/'

# Create your views here.
def index(request: HttpRequest):
    context = {}
    return render(request, 'index.html', context=context)

def votedata(request: HttpRequest):
    match = Match.getCurrent()
    ip_addr, is_routable = get_client_ip(request)
    query = Vote.objects.filter(ip_addr=ip_addr).filter(match=match)
    vote = query.first().getVote() if query.exists() else '0'

    if request.method == 'POST' and 'vote' in request.POST:
        vote = request.POST['vote']
        if not query.exists(): # this ip hasn't voted yet
            match.vote(ip_addr, vote)

    context = {
        'base_url_icon': BASE_URL_ICON,
        'match': match,
        'voted': vote
    }
    return render(request, 'votedata.html', context=context)

def scoredata(request: HttpRequest):
    match = Match.getCurrent()
    # match.refresh_from_db(fields=['scoreA', 'scoreB'])
    context = {
        'scoreA': match.scoreA,
        'scoreB': match.scoreB
    }
    return render(request, 'scoredata.html', context=context)


class TopView(generic.ListView):
    model = Item
    paginate_by = 30

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['base_url_icon'] = BASE_URL_ICON
        return context