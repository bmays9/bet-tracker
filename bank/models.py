from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_account')
    updated_on = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user}: £ {self.balance}"