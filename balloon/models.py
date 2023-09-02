from django.db import models
from accounts.models import User


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Recent_Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    images = models.ImageField(upload_to='media/product')
    images_1 = models.ImageField(upload_to='media/product')
    images_2 = models.ImageField(upload_to='media/product')
    images_3 = models.ImageField(upload_to='media/product')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    is_stock = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class ReviewRating(models.Model):
    product = models.ForeignKey(Recent_Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.subject
