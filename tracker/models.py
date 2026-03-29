from django.db import models

class Coin(models.Model):
    coin_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    threshold = models.DecimalField(max_digits=12, decimal_places=2)
    tolerance = models.DecimalField(max_digits=12, decimal_places=2)
    alert_above = models.BooleanField(default=False)

class PriceSnapshot(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    coin = models.ForeignKey("Coin", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    notified = models.BooleanField(default=False)
