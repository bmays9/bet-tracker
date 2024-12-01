from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from .models import Bank


# Create your views here.
class bank_list(ListView):
    """
    Renders the Bank account rankings list page
    """

    queryset = Bank.objects.all().order_by("-balance") 
    template_name = "bank/list.html"
    context_object_name = 'accounts'
