from . import views
from django.urls import path


urlpatterns = [
    path('', views.admiin, name='admiin'),
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # path('category/<str:category_name>/', views.category_products, name='category_products'),


    path('admin-panel/add-product/', views.add_product, name='add_product'),
    path('toggle_payment_status/<int:order_id>/', views.toggle_payment_status, name='toggle_payment_status'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),




]