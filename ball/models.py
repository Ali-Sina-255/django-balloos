from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    amount = models.IntegerField()
    created_at = models.DateTimeField(max_length=100)
    updated_at = models.DateTimeField(max_length=501)

    def __str__(self):
        return self.category_name


class Recent_Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, unique=True)
    images = models.ImageField(upload_to='media/product')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
