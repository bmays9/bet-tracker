from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column
from django.forms import inlineformset_factory
from .models import Bet, Line

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('stake',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
        Row(
            Column('stake', css_class='col-md-4 stake-input'),
        ),
        )
   

class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = ('home_team', 'away_team',
            'prediction', 'odds')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # Disable the form tag for inline formsets
        self.helper.layout = Layout(
            Row(
                Column('home_team', css_class='col-md-3'),
                Column('away_team', css_class='col-md-3'),
            ),
            Row(
                Column('prediction', css_class='col-md-3'),
                Column('odds', css_class='col-md-1'),
            )
        )

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

LineAddFormSet = inlineformset_factory(
    Bet,    # Parent Model
    Line,   # Child Model
    form = LineForm,
    extra=6,
    can_delete = True
    )
