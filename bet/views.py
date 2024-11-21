from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Count
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Bet, Line 
from bank.models import Bank
from .forms import BetForm, LineForm, EditBetForm, LineFormSet, LineAddFormSet

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
                context['user_balance'] = 0.00  
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
        line_formset = LineAddFormSet(data=request.POST)
        
        if bet_form.is_valid() and line_formset.is_valid():

            bet = bet_form.save(commit=False)
            bet.punter = request.user
            bet.save()

            line_items = line_formset.save(commit=False)
            for line_item in line_items:
                line_item.bet = bet
                line_item.save()
                       
            # Display message to the user
            messages.add_message(request, messages.SUCCESS, 'Your bet has been added')
            # Reset form
            bet_form = BetForm()
            line_formset = LineAddFormSet()
    else: 
        bet_form = BetForm()
        line_formset = LineAddFormSet()
    
    return render(
        request, 
        'bet/add_bet.html',
        {
            'bet_form': bet_form,
            'line_formset': line_formset
        }
    )


def delete_bet(request, id):
    '''
    View to delete comment
    '''
    queryset = Bet.objects.filter(status=0)
    bet = get_object_or_404(queryset, id=id)
    
    if bet.punter == request.user:
        bet.delete()
        print("Bet delete?")
        return redirect('home')
    
    return HttpResponseRedirect(reverse('bet_delete', args=[id]))

def update_bet(request, id):
    """
    Display a single model: bet with all lines details so that it can be edited or updated
    Only bets with status 'pending' can be edited
    
    template = bet/update_bet.html
    """
    queryset = Bet.objects.filter(status=0)
    bet = get_object_or_404(queryset, id=id) 
    print("bet object is..")
    print (bet)
    line_count = bet.lines.count()
    print(line_count)

    if request.method == 'POST':

        edit_bet_form = EditBetForm(data=request.POST, instance=bet)
        line_formset = LineFormSet(data=request.POST, instance=bet)
       
        if edit_bet_form.is_valid() and line_formset.is_valid() and bet.punter == request.user:
            
            print("It's all valid")
            edit_bet_form.save()
            line_formset.save()
            #check if bet is settled
            
            
            return render(request, "bet/update_bet.html", {"edit_bet_form": edit_bet_form, "line_formset": line_formset, "success": True})

        else:
            print("It's not valid")
            print(edit_bet_form.errors)
            print(line_formset.errors)
    else: 
        #populate forms with existing data
        edit_bet_form = EditBetForm(instance=bet)
        line_formset = LineFormSet(instance=bet)
        
    return render(
        request,
        "bet/update_bet.html",
        {
        "edit_bet_form": edit_bet_form,
        "line_formset": line_formset,
        "line_count": line_count,
        })
        
   
       
