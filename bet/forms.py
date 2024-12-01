from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset, Div
from crispy_forms.bootstrap import InlineField
from django.forms import inlineformset_factory, formset_factory
from .models import Bet, Line


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('stake',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class
        self.helper.layout = Layout(
            Fieldset(
                'Enter stake',
                'stake',
                ),
                )


class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = (
            'home_team',
            'away_team',
            'prediction',
            'odds'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # No form tags for formsets
        self.helper.layout = Layout(
            Fieldset(
                'home_team',
                'away_team',
                'prediction',
                'odds',
            )
        )


class EditBetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = (
            'stake',
            'status',
            'settled_amount'
        )

    def __init__(self, *args, **kwargs):
        super(EditBetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


# LineFormSet used when updating a bet.
LineFormSet = inlineformset_factory(
    Bet,    # Parent Model
    Line,   # Child Model
    fields=[
        'home_team', 'away_team',
            'prediction', 'odds', 'match_result', 'status'
        ],
    extra=0,
    can_delete=True
    )

# LineAddFormSet used when addint a bet. 6 lines available
LineAddFormSet = inlineformset_factory(
    Bet,    # Parent Model
    Line,   # Child Model
    form=LineForm,
    extra=6,
    can_delete=True
    )


class LineAddFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            Fieldset(
                'Add data for each line',
                'home_team',
                'away_team',
                'prediction',
                'odds',
                css_id='line-fields'
            ),
            )
        self.render_required_fields = True
