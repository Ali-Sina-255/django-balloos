from django.contrib import admin
from .models import Recent_Product, Category, ReviewRating


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'amount', 'created_at')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Recent_Product)
admin.site.register(ReviewRating)
