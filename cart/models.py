from django.db import models
from balloon.models import Recent_Product


# Create your models here.
class Card(models.Model):
    card_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_id


class CartItem(models.Model):
    product = models.ForeignKey(Recent_Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product_name
import random 

def play(user, computer):
    