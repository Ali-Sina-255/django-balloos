from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('product_details/category/<int:pk>/', views.product_details, name='product_details'),
path('submit_review/category/<int:pk>/', views.submit_review, name='submit_review'),
path('blog/', views.blog , name='blog'),
path('blog_details/<int:pk>/', views.blog_details, name='blog_details'),
path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
path('blog/our_team/', views.out_teams, name='our_team'),
path('error_page/', views.error_page, name='error_page'),
path('blog/product_list/', views.product_list, name='product_list'),
]