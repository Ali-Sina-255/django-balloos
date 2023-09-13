from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_card, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_card, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]
