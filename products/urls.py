from django.urls import path
from django.http import HttpResponse
from django.urls import reverse

from .views import (
    product_detail_view, 
    product_create_view, 
    product_delete_view, 
    product_list_view, 
    )
app_name = "products"
urlpatterns = [
    path('', product_list_view, name="product_list_view"),
    path('create/', product_create_view),
    path('<int:id>/', product_detail_view, name='product_detail/'),
    path('<int:id>/delete/', product_delete_view, name='product_delete'),
]