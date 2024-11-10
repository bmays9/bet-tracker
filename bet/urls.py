from . import views
from django.urls import path

urlpatterns = [
    path('', views.OpenBets.as_view(), name='home'),
]