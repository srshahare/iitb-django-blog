from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogHome, name="BlogHome"),
    path('create', views.blogCreate, name="Blog Post"),
    path('dashboard', views.blogDashboard, name="Blog Dashboard"),
    path('dashboard/delete/<str:slug>', views.deleteBlog, name="Delete Blog"),
    path('<str:slug>', views.blogPost, name="Blog Post"),
]
