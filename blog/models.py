from django.db import models
from profiles.models import MyUserModel

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    author = models.CharField(max_length=20, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="posts")
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(MyUserModel, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.user




