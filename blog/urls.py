from django.urls import path, reverse
from django.http import HttpResponse

from .views import (
    blog_detail_view, 
    blog_create_view, 
    blog_confirm_delete_view, 
    blog_list_view, 
    ArticleDetailView,
    ArticleCreateView,
    ArticleConfirmDeleteVew, 
    ArticleListView, 
    )

    # path for class-based views: 
        # <app_name>/<model_name>_list.html


app_name = "blog"
urlpatterns = [
    path('', blog_list_view, name="blog_list"),
    path('create/', blog_create_view, name="blog_create"),
    path('<int:id>/', blog_detail_view, name='blog_detail/'),
    path('<int:id>/delete/', blog_confirm_delete_view, name='blog_delete'),

    path('article', ArticleListView.as_view(), name="article_list"),
    path('article_create/', ArticleCreateView.as_view(), name="article_create"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:id>/delete/', ArticleConfirmDeleteVew.as_view(), name='article_delete'),
# alt: path('', ArticleDetailview.as_view(template_name='template.html', name='name')),
]