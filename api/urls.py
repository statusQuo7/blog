from django.urls import path
from .views import (
    PostListView, 
    CategoryListView, 
    PostDetailUpdateView, 
    CategoryDetailView, 
    PostCreateView,
    CategoryCreateView,
)



app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name = "anna"),
    path('categories/', CategoryListView.as_view(), name = "elza"),
    path('post/detail/<int:pk>/', PostDetailUpdateView.as_view(), name = "olaf"),
    path('category/detail/<int:category_id>/', CategoryDetailView.as_view(), name = "hans"),
    path('post/create/', PostCreateView.as_view(), name = "sven"),
    path('category/create/', CategoryCreateView.as_view(), name = "vladimir"),
   
]
