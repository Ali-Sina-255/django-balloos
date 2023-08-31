from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/category/<int:pk>/', views.product_details, name='product_details'),
]