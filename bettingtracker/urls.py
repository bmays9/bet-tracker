"""
URL configuration for bettingtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bank import views as bank_views
from bet import views as bet_views

urlpatterns = [
    path('accounts/', include("allauth.urls")),
    path('add/', bet_views.add_bet, name='add'),
    path('admin/', admin.site.urls),
    path('bank/', bank_views.bank_list.as_view(), name='bank'),
    path('summernote/', include('django_summernote.urls')),
    path('', include("bet.urls"), name='bet-urls'),
]
