
from django.urls import path
from .views import (
    AboutView, 
    CommentFormView, 
    ContactFormView, 
    PostDetailView, 
    create_post, 
    search, 
    PostListView
)


app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name = "drop"),
    path('contact/', ContactFormView.as_view(), name = "contact"),
    path('about/', AboutView.as_view(), name = "about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post"),
    path('comment/create/', CommentFormView.as_view(), name = "comment_create" ),
    path('search/', search, name = "search"),
    path('create_post/', create_post, name = "create_post"),

]

