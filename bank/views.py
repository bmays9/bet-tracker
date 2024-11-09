from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_bank(request):
    return HttpResponse("Hello, Bank app!")