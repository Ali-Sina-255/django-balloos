from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Recent_Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, unique=True)
    images = models.ImageField(upload_to='media/product')
    images_1 = models.ImageField(upload_to='media/product')
    images_2 = models.ImageField(upload_to='media/product')
    images_3 = models.ImageField(upload_to='media/product')
    description = models.TextField(blank=True)
    amount = models.IntegerField()
    price = models.IntegerField()
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Party_Accessories(models.Model):
    accessories_name = models.CharField(max_length=255, unique=True)
    images = models.ImageField(upload_to='media/product')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accessories_name

