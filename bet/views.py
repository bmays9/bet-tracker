from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from django.views.generic import ListView
from .models import Bet, Line 
from bank.models import Bank
from .forms import BetForm, LineForm

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


def add_bet(request):
    """
    Renders the add bet page
    """ 
    if request.method == 'POST':
        bet_form = BetForm(data=request.POST)
        line_form = LineForm(data=request.POST)
        print("Received a post request")
        
        if bet_form.is_valid() and line_form.is_valid():

            print("It's valid")
            #bet_data=bet_form.cleaned_data
            #line_data=line_form.cleaned_data

            #bet.stake = bet_data['stake']
            #bet.punter = request.user
            
            bet = bet_form.save(commit=False)
            bet.punter = request.user
            bet.save()
            

            print(bet_form.cleaned_data)
            print(line_form.cleaned_data)
            #line.home_team = line_data['home_team']
            #line.away_team = line_data['away_team']
            #line.prediction = line_data['prediction']
            #line.odds = line_data['odds']
            line = line_form.save(commit=False)

            line.bet = bet
            
            line.save()
            
            

    
    else: 
        bet_form = BetForm()
        line_form = LineForm()

    
    return render(
        request, 
        'bet/add_bet.html',
        {
            'bet_form': bet_form,
            'line_form': line_form
        }
    )