from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bet, Line
# Register your models here.


@admin.register(Bet)
class BetAdmin(SummernoteModelAdmin):
    """
    Configuration for Bet Model in the admin pages
    """
    list_display = (
        'punter', 'stake', 'settled_amount', 'updated_on', 'status')
    search_fields = ['punter', 'status']
    list_filter = ('punter', 'created_on', 'status')


@admin.register(Line)
class LineAdmin(SummernoteModelAdmin):
    """
    Configuration for Bank Model in the admin pages
    """
    list_display = (
        'home_team', 'away_team', 'prediction', 'match_result', 'status')
    search_fields = ['home_team', 'away_team', 'status']
    list_filter = ('created_on', 'status', 'bet')
