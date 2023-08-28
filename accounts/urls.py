from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
    path('register_user/', views.register_user, name='register_user'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('contact/', views.contact, name='contact'),
]
