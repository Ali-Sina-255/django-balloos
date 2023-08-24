from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
    path('register_user/', views.register_user, name='register_user'),
]
