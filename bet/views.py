from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Count
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Bet, Line
from bank.models import Bank
from .forms import BetForm, LineForm, EditBetForm, LineFormSet
from .forms import LineAddFormSet, LineAddFormSetHelper
from decimal import Decimal


class OpenBets(ListView):
    """
    Renders the Open Bets view in "View Bets" page
    """

    # queryset = Bet.objects.filter(status=0).order_by("updated_on")
    template_name = "bet/bets.html"
    context_object_name = 'open_bets'

    def get_queryset(self):
        queryset = Bet.objects.filter(
            status=0).order_by(
                "-updated_on").annotate(
                    line_count=Count('lines')).prefetch_related('lines')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            try:
                user_bank = Bank.objects.get(user=user)
                context['user_balance'] = user_bank.balance

            except Bank.DoesNotExist:
                context['user_balance'] = 0.00
        else:
            context['user_balance'] = ""

        return context


class SettledBets(ListView):
    """
    Renders the Settled Bets view in "View Bets" page
    """

    # queryset = Bet.objects.filter(status=0).order_by("updated_on")
    template_name = "bet/bets.html"
    context_object_name = 'open_bets'

    def get_queryset(self):
        queryset = Bet.objects.exclude(status=0).order_by("-updated_on")
        return queryset.annotate(
            line_count=Count('lines')).prefetch_related('lines')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            try:
                user_bank = Bank.objects.get(user=user)
                context['user_balance'] = user_bank.balance

            except Bank.DoesNotExist:
                context['user_balance'] = 0.00
        else:
            context['user_balance'] = ""

        return context


def add_bet(request):
    """
    Handles the Add Bet page
    template = bet/add_bet.html
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
            messages.add_message(
                request,
                messages.SUCCESS, (
                    'SUCCESS! Your bet has been added.'
                    'Either add another bet or return to the home page'
                    )
                )
            # Reset form
            bet_form = BetForm()
            line_formset = LineAddFormSet()

    else:  # Not a Post request
        bet_form = BetForm()
        line_formset = LineAddFormSet()

    return render(
        request,
        'bet/add_bet.html',
        {
            'bet_form': bet_form,
            'line_formset': line_formset,
        }
    )


def delete_bet(request, id):
    '''
    Handles the delete bet process
    '''
    queryset = Bet.objects.filter(status=0)
    bet = get_object_or_404(queryset, id=id)

    if bet.punter == request.user:
        bet.delete()
        # Add a success message and redirect
        messages.success(
            request,
            'SUCCESS! Your bet has been deleted')

        return redirect('bets')

    return HttpResponseRedirect(reverse('bet_delete', args=[id]))


def update_bet(request, id):
    """
    Displays a bet with all lines details so that it can be edited or updated
    Only bets with status 'pending' can be edited
    template = bet/update_bet.html
    """
    queryset = Bet.objects.filter(status=0)
    bet = get_object_or_404(queryset, id=id)
    line_count = bet.lines.count()

    if request.method == 'POST':

        edit_bet_form = EditBetForm(data=request.POST, instance=bet)
        line_formset = LineFormSet(data=request.POST, instance=bet)
        user = request.user
        # check user is authenticated

        if user.is_authenticated:
            # check forms are valid
            if (
                edit_bet_form.is_valid()
                and line_formset.is_valid()
                and bet.punter == user
            ):

                # check if bet is settled
                if bet.status != 0:  # If status is not pending, adjust balance
                    try:
                        user_bank = Bank.objects.get(user=user)
                    except Bank.DoesNotExist:
                        user_bank = Bank(
                            user=user, balance=Decimal(0.00), is_active=True)

                    # update user's bank balance
                    user_bank.balance = user_bank.balance + (
                        bet.settled_amount - bet.stake)
                    user_bank.save()
                    edit_bet_form.save()
                    line_formset.save()

                    # Add a success message and redirect
                    messages.success(
                        request,
                        'Bet settled and balance updated successfully!')
                    return redirect('bets')

                else:
                    # Bet is still pending but form is valid.
                    # Save data and send message to the user

                    edit_bet_form.save()
                    line_formset.save()
                    messages.add_message(request, messages.SUCCESS, (
                        'Your changes have been saved. '
                        'The bet is still pending so your balance is unchanged'
                        ))

                    return render(
                        request,
                        "bet/update_bet.html",
                        {
                            "edit_bet_form": edit_bet_form,
                            "line_formset": line_formset,
                            "success": True
                        }
                        )

            else:
                messages.add_message(request, messages.SUCCESS, (
                    'The data is invalid, please correct it and try again'
                    )
                )

    else:
        # populate forms with existing data

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


def homepage(request):
    return render(request, 'bet/index.html')
