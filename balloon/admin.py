from django.contrib import admin
from .models import Recent_Product, Category, ReviewRating, Blog, Comment, \
    OurTeam, Weekly_Hots


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'amount', 'created_at')


admin.site.register(Category, CategoryAdmin)


class Recent_product(admin.ModelAdmin):
    list_display = ('product_name', 'recent_product_image', 'price', 'is_stock')


admin.site.register(Recent_Product, Recent_product)
admin.site.register(ReviewRating)


class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Blog, AdminBlog)

admin.site.register(Comment)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team_image', 'phone_number')
    list_display_links = ('team_image', 'name', 'position')


admin.site.register(OurTeam, TeamAdmin)


class Weekly_Admin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'created_at')
    list_display_links = ('product_name', 'price')


admin.site.register(Weekly_Hots, Weekly_Admin)
