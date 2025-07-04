from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home' ),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.category_products, name='category_products'),  # اضافه شد
]