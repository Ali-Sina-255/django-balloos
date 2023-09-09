from django.db import models
from balloon . models import Recent_Product

# Create your models here.
class Card_item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Recent_Product, on_delete=models.CASCADE)

class CartItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Recent_Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    