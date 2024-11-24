from django.test import TestCase
from .forms import BetForm, LineForm, EditBetForm, LineFormSet, LineAddFormSet 

class TestBetForm(TestCase):

    def test_betform_is_valid(self):
        bet_form = BetForm({
            'stake': 3.22,
            'user': 'Tester1',
            })
        self.assertTrue(bet_form.is_valid(), msg='Test fail. BetForm is not valid') 

    def test_betform_is_invalid(self):
        bet_form = BetForm({
            'stake': '-3.21',
            'user': 'Tester1',
            })

        self.assertFalse(bet_form.is_valid(), msg='Test fail. BetForm with negative stake is valid') 
    
    def test_betform_is_invalid_stake_zero(self):
        bet_form = BetForm({
            'stake': '0.00',
            'user': 'Tester1',
            })

        self.assertFalse(bet_form.is_valid(), msg='Test fail. BetForm with zero stake is valid') 

    def test_betform_with_minimum_stake(self):
        bet_form = BetForm({
            'stake': '0.01',
            'user': 'Tester1',
            })

        self.assertTrue(bet_form.is_valid(), msg='Test fail. BetForm with 0.02 stake is invalid') 
