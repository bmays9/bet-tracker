from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import inlineformset_factory
from .models import Bet, Line

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('stake',)

class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = ('home_team', 'away_team',
            'prediction', 'odds')

class EditBetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('stake', 'status', 'settled_amount')

    def __init__(self, *args, **kwargs):
        super(EditBetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))

LineFormSet = inlineformset_factory(
    Bet,    # Parent Model
    Line,   # Child Model
    fields=['home_team', 'away_team','prediction','odds', 'match_result', 'status'],
    extra=1,
    can_delete = True 
    )
