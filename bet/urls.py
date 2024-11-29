from . import views
from django.urls import path
from .views import add_bet

urlpatterns = [
    path('add/', add_bet, name='add_bet'),
    path('delete/<uuid:id>', views.delete_bet, name='delete_bet'),
    path('settled/', views.SettledBets.as_view(), name='settled_list'),
    path('update/<uuid:id>/', views.update_bet, name='update_bet'),
    path('', views.OpenBets.as_view(), name='bets'),    
]