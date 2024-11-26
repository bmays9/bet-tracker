from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
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

class TestAddBetViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="mySupername",
            password="aPassword",
            email="test@test.com"
        )
        self.bet = Bet(
            punter=self.user, 
            stake="10.00",
        )
        self.bet.save()
        self.line = Line(
            home_team="Home Utd", 
            away_team="Away Town",
            prediction="1",
            odds="3.12",
            
        )
        self.line.save()

