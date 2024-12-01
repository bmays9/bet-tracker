from django.test import TestCase
from .forms import BetForm, LineForm, EditBetForm, LineFormSet, LineAddFormSet


class TestBetForm(TestCase):

    def test_betform_is_valid(self):
        bet_form = BetForm({
            'stake': 3.22,
            'user': 'Tester1',
            })
        self.assertTrue(bet_form.is_valid(), msg='Fail. BetForm is not valid')

    def test_betform_is_invalid(self):
        bet_form = BetForm({
            'stake': '-3.21',
            'user': 'Tester1',
            })
        self.assertFalse(
            bet_form.is_valid(), msg='BetFormm with -ve stake valid')

    def test_betform_is_invalid_stake_zero(self):
        bet_form = BetForm({
            'stake': '0.00',
            'user': 'Tester1',
            })
        self.assertFalse(
            bet_form.is_valid(), msg='Fail. BetForm with zero stake is valid')

    def test_betform_with_minimum_stake(self):
        bet_form = BetForm({
            'stake': '0.01',
            'user': 'Tester1',
            })
        self.assertTrue(
            bet_form.is_valid(), msg='Fail. BetForm with 0.01 stake invalid')

    def test_betform_with_maximum_stake(self):
        bet_form = BetForm({
            'stake': '99999999.99',
            'user': 'Tester1',
            })
        self.assertTrue(
            bet_form.is_valid(), msg='Fail. BetForm with max stake is invalid')

    def test_betform_with_stake_too_long(self):
        bet_form = BetForm({
            'stake': '123456789.01',
            'user': 'Tester1',
            })
        self.assertFalse(
            bet_form.is_valid(), msg='Fail. BetForm 11 digit stake is invalid')

    def test_betform_with_empty_stake(self):
        bet_form = BetForm({
            'stake': '',
            'user': 'Tester1',
            })
        self.assertFalse(
            bet_form.is_valid(), msg='Fail. BetForm with empty stake is valid')


class TestLineForm(TestCase):
    # Test cases for lines when adding a new bet

    def test_lineform_is_valid(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '2.34',
            })
        self.assertTrue(
            line_form.is_valid(), msg='Test fail. LineForm is not valid')

    def test_lineform_max_len_home_team(self):
        line_form = LineForm({
            'home_team': 'TeamTeamTeamTeam',
            'away_team': 'TeamA',
            'prediction': '2',
            'odds': '2.34',
            })
        self.assertTrue(
            line_form.is_valid(), msg='Fail. LF not valid with max len Home')

    def test_lineform_empty_home_team(self):
        line_form = LineForm({
            'home_team': '',
            'away_team': 'Away United',
            'prediction': '3',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with empty HomeTeam')

    def test_lineform_inv_len_home_team(self):
        line_form = LineForm({
            'home_team': 'TeamTeamTeamTeamHomeHome',
            'away_team': 'Awayteam',
            'prediction': '3',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with > max length Home')

    def test_lineform_max_len_away_team(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamTeamTeamTeam',
            'prediction': '3',
            'odds': '2.34',
            })
        self.assertTrue(
            line_form.is_valid(), msg='Fail. LF invalid with max length Away')

    def test_lineform_empty_away_team(self):
        line_form = LineForm({
            'home_team': 'Home Town',
            'away_team': '',
            'prediction': '3',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with empty AwayTeam')

    def test_lineform_inv_len_away_team(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamTeamTeamTeamA',
            'prediction': '0',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with > max len AwayTeam')

    def test_lineform_invalid_prediction(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '4',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with invalid Prediction')

    def test_lineform_empty_prediction(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with empty Prediction')

    def test_lineform_text_prediction(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': 'home',
            'odds': '2.34',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with text Prediction')

    def test_lineform_no_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF  valid with no odds')

    def test_lineform_max_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '9999999.999',
            })
        self.assertTrue(
            line_form.is_valid(), msg='Fail. LF is invalid with max odds')

    def test_lineform_too_long_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '12345678.901',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with too long odds')

    def test_lineform_too_many_decimal_places(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '12.45678',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF  valid with 5 dec places odds')

    def test_lineform_too_low_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '0.999',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with odds=0.999')

    def test_lineform_negative_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '-5.654',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with negative odds')

    def test_lineform_zero_odds(self):
        line_form = LineForm({
            'home_team': 'TeamH',
            'away_team': 'TeamA',
            'prediction': '1',
            'odds': '0',
            })
        self.assertFalse(
            line_form.is_valid(), msg='Fail. LF valid with zero odds')


class TestEditBetForm(TestCase):

    def test_editbetform_is_valid(self):
        editbet_form = EditBetForm({
            'stake': 3.22,
            'status': '1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertTrue(
            editbet_form.is_valid(), msg='Test fail. EditBetForm is not valid')

    def test_editbetform_is_invalid(self):
        editbet_form = EditBetForm({
            'stake': '-3.21',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail EBF with -ve stake is valid')

    def test_editbetform_is_invalid_stake_zero(self):
        editbet_form = EditBetForm({
            'stake': '0.00',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail. EBF with zero stake is valid')

    def test_editbetform_with_minimum_stake(self):
        editbet_form = EditBetForm({
            'stake': '0.01',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertTrue(
            editbet_form.is_valid(), msg='Fail. EBF & 0.01 stake is invalid')

    def test_editbetform_with_maximum_stake(self):
        editbet_form = EditBetForm({
            'stake': '99999999.99',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertTrue(
            editbet_form.is_valid(), msg='Fail. EBF with max stake is invalid')

    def test_editbetform_with_stake_too_long(self):
        editbet_form = EditBetForm({
            'stake': '123456789.01',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '0',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail. EBF with 11 digit stake valid')

    def test_editbetform_with_empty_stake(self):
        editbet_form = EditBetForm({
            'stake': '',
            'user': 'Tester1',
            'settled_amount': '0.00',
            'status': '1',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail. EBF with empty stake is valid')

    def test_editbetform_with_negative_settled_amount(self):
        editbet_form = EditBetForm({
            'stake': '10.00',
            'user': 'Tester1',
            'settled_amount': '-2.04',
            'status': '1',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail. EBF w/ -ve set amount valid')

    def test_editbetform_with_invalid_settled_amount(self):
        editbet_form = EditBetForm({
            'stake': '10.00',
            'user': 'Tester1',
            'settled_amount': '123456789.01',
            'status': '1',
            })
        self.assertFalse(
            editbet_form.is_valid(), msg='Fail. EBF set amount too long valid')
