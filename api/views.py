from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from blog.models import Post, Category
from .serializers import (
    PostListSerializer, 
    CategoryListSerializer, 
    PostDetailCreateUpdateSerializer, 
    CategoryCreateSerializer,
)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailCreateUpdateSerializer
    lookup_field = "pk"

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return Post.objects.filter(category_id = category_id)

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailCreateUpdateSerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer