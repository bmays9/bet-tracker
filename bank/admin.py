from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bank
# Register your models here.


@admin.register(Bank)
class BankAdmin(SummernoteModelAdmin):
    """
    Configuration for Bank Model in the admin pages
    """
    list_display = ('user', 'balance', 'updated_on', 'is_active')
    search_fields = ['user']
    list_filter = ('user', 'is_active')
