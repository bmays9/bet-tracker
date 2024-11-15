from . import views
from django.urls import path
from .views import add_bet

urlpatterns = [
    path('add/', add_bet, name='add_bet'),
    path('settled/', views.SettledBets.as_view(), name='settled_list'),
    path('', views.OpenBets.as_view(), name='home'),
]