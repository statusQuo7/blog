from django.urls import path

from .views import signup

app_name = "profiles"

urlpatterns = [
    path('signup/', signup, name = "signup")
]