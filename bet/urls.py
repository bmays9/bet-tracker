from . import views
from django.urls import path

urlpatterns = [
    path('', views.OpenBets.as_view(), name='home'),
    path('settled/', views.SettledBets.as_view(), name='settled_list'),
]