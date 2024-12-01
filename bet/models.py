from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import uuid

RESULT = ((0, "Pending"), (1, "Home"), (2, "Away"), (3, "Draw"))
STATUS = ((0, "Pending"), (1, "Win"), (-1, "Lose"))


# Validation functions
def positiveAmountValidator(value):
    """
    Validates the value is greater than zero.
    Returns True or raises a ValidationError
    """
    if value > 0.00:
        return True
    else:
        raise ValidationError("Stake amount must be greater than zero")


def settledAmountValidator(value):
    """
    Validates the amount is greater than or equal to zero.
    Returns True or raises a ValidationError.
    """
    if value >= 0.00:
        return True
    else:
        raise ValidationError(
            "Settled amount must be greater than or equal to zero")


class Bet(models.Model):
    """
    Defines the Bet Model
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    punter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="placed_by")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    stake = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[positiveAmountValidator])
    status = models.IntegerField(choices=STATUS, default=0)
    settled_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[settledAmountValidator])

    class Meta:
        """
        Inner class of the Bet model - orders by creation date
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the Bet Model
        """
        return f"{self.punter} | Stake: {self.stake} | {self.id}"


class Line(models.Model):
    """
    Defines the Line Model
    """
    home_team = models.CharField(max_length=16)
    away_team = models.CharField(max_length=16)
    prediction = models.IntegerField(choices=RESULT, default=1)
    odds = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(1.00)]
    )
    match_result = models.IntegerField(choices=RESULT, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bet = models.ForeignKey(
        Bet, on_delete=models.CASCADE, related_name="lines")

    class Meta:
        """
        Inner class of the Line model - orders by creation date
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the Line Model
        """
        return f"{self.home_team} v {self.away_team} | 102: {self.prediction}"
