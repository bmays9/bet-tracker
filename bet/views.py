from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from django.views.generic import ListView
from .models import Bet, Line

# Create your views here.
class OpenBets(ListView):
    """
    Renders the open bets page
    """ 
         
    # queryset = Bet.objects.filter(status=0).order_by("updated_on")
    template_name = "bet/open_bets.html"
    context_object_name = 'open_bets'
    # paginate_by = 5
    
    def get_queryset(self):
        queryset = Bet.objects.filter(status=0).order_by("-updated_on")
        return queryset.annotate(line_count=Count('lines')).prefetch_related('lines')
