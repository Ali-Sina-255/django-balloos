from django.contrib import admin
from .models import Recent_Product, Category,ReviewRating, Blog, Comment


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'amount', 'created_at')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Recent_Product)
admin.site.register(ReviewRating)

class AdminBlog(admin.ModelAdmin):
    prepopulated_fields ={"slug":("name",)}

admin.site.register(Blog, AdminBlog)

admin.site.register(Comment)