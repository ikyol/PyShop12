from django.urls import path
from product.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('<str:slug>/', product_list, name='list'),
    path('product/<int:id>/', product_detail, name='detail'),
    path('product/create/', create_product, name='create-product'),
    path('product/update/<int:id>/', update_product, name='update_product'),
    path('product/delete/<int:id>/', delete_product, name='delete_product'),
    ]