from django.contrib import admin
from .models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "create_date"]
    list_filter = ["category"]
    search_fields = ["title", "description"]
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)

