from django.test import TestCase
from .forms import BetForm, LineForm, EditBetForm

class TestBetForm(TestCase):

    def test_betform_is_valid(self):
        bet_form = BetForm({'stake': 3.22})
        
        self.assertTrue(bet_form.is_valid(), msg='Test fail. BetForm is not valid') 

    def test_betform_is_invalid(self):
        bet_form = BetForm({'stake': '-3.21'})

        self.assertFalse(bet_form.is_valid(), msg='Test fail. BetForm is valid') 

class TestLineForm(TestCase):
    
    def test_lineform_is_valid(self):
        line_form = LineForm(
            {
            'home_team': "Aberdeen",
            'away_team': "Rangers",
            'prediction': "Home",
            'odds': 1.45,
            })
    
    def test_lineform_is_invalid(self):
        line_form = LineForm(
            {
            'home_team': "",
            'away_team': "Rangers",
            'prediction': "Home",
            'odds': 1.45,
            })
        self.assertTrue(bet_form.is_invalid(), msg='Test fail. LineForm is valid when home team is empty') 

