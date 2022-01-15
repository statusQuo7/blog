from rest_framework import serializers
from blog.models import Post, Category



class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ["description",]

class PostDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"