from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/category/<int:pk>/', views.product_details, name='product_details'),
    path('submit_review/category/<int:pk>/', views.submit_review, name='submit_review'),
]