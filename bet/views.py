from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_bet(request):
    return HttpResponse("Hello, I'm having a bet!")
