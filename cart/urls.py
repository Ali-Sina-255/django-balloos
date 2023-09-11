from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart ,name='cart' ),
    path('add_cart/<int:product_id>/', views.add_card, name='add_cart'),
]
