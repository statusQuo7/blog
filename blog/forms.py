from django import forms
from django.db import models
from django.forms import fields
from .models import Comment, Post



class FeedbackForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=20)
    message = forms.CharField(max_length=200,widget=forms.TextInput({}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["date", "user"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"






    