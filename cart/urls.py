from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/', views.add_cart, name='add_cart')
]
