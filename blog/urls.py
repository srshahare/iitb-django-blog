from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogHome, name="BlogHome"),
    path('<str:slug>', views.blogPost, name="Blog Post"),
]
