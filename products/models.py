from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=400)
    threshold = models.DecimalField(max_digits=6, decimal_places=2)
    tolerance = models.DecimalField(max_digits=5, decimal_places=2)

class PriceSnapshot(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
