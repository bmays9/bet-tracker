from django.db import models
from django.contrib.auth.models import User
import uuid

RESULT = ((0, "Pending"), (1, "Home"), (2, "Away"), (3, "Draw"))
STATUS = ((0, "Pending"), (1, "Win"), (-1, "Lose"))

# Create your models here.
class Bet(models.Model):
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    punter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="placed_by")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    stake = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=0)
    settled_amount =  models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.punter} | Stake: {self.stake} | {self.id}"


class Line(models.Model):
    home_team = models.CharField(max_length=16)
    away_team = models.CharField(max_length=16)
    prediction = models.IntegerField(choices=RESULT, default=1)
    odds = models.DecimalField(max_digits=10, decimal_places=3)
    match_result = models.IntegerField(choices=RESULT, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE, related_name="lines")


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.home_team} v {self.away_team} | 102: {self.prediction}  "
