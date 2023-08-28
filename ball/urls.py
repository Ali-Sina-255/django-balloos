from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('our_blog/', views.our_blog, name='our_blog'),
]
