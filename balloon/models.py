from django.db import models
from accounts.models import User
from django.utils.html import format_html


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

    def recent_product_image(self):
        return format_html("<img width=100;height=75; style='border-radius:5px' src='{}'>".format(self.images.url))

    recent_product_image.short_description = 'Images'


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


class Party_Accessories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/')
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    images = models.ImageField(upload_to='media/blog')
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment_name} {self.comment_body}'


class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    images = models.ImageField(upload_to='media/team/')
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def team_image(self):
        return format_html("<img width=100;height=75; style='border-radius:5px' src='{}'>".format(self.images.url))

    team_image.short_description = 'Images'
