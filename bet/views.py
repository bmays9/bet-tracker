from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from django.views.generic import ListView
from .models import Bet, Line 
from bank.models import Bank

# Create your views here.
class OpenBets(ListView):
    """
    Renders the open bets page
    """ 
         
    # queryset = Bet.objects.filter(status=0).order_by("updated_on")
    template_name = "bet/index.html"
    context_object_name = 'open_bets'
        
    def get_queryset(self):
        queryset = Bet.objects.filter(status=0).order_by("-updated_on").annotate(line_count=Count('lines')).prefetch_related('lines')
        return queryset
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            try:
                user_bank = Bank.objects.get(user=user)
                context['user_balance'] = user_bank.balance
            
            except Bank.DoesNotExist:
                context['user_balance'] = None  
        else:
            context['user_balance'] = None
        return context

class SettledBets(ListView):
    """
    Renders the settled bets page
    """ 
         
    # queryset = Bet.objects.filter(status=0).order_by("updated_on")
    template_name = "bet/index.html"
    context_object_name = 'open_bets'
        
    def get_queryset(self):
        queryset = Bet.objects.exclude(status=0).order_by("-updated_on")
        return queryset.annotate(line_count=Count('lines')).prefetch_related('lines')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            try:
                user_bank = Bank.objects.get(user=user)
                context['user_balance'] = user_bank.balance
            
            except Bank.DoesNotExist:
                context['user_balance'] = None  
        else:
            context['user_balance'] = None
        return context
