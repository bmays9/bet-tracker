from .models import Bet, Line
from django import forms

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('stake',)

class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = ('home_team', 'away_team',
            'prediction', 'odds')