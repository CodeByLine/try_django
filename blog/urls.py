from django.urls import path, reverse
from django.http import HttpResponse

from .views import (
    blog_detail_view, 
    blog_create_view, 
    blog_confirm_delete_view, 
    blog_list_view, 
    )
app_name = "blog"
urlpatterns = [
    path('', blog_list_view, name="blog_list"),
    path('create/', blog_create_view, name="blog_create"),
    path('<int:id>/', blog_detail_view, name='blog_detail/'),
    path('<int:id>/delete/', blog_confirm_delete_view, name='blog_delete'),
]