from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("login/", views.login, name="BlogLogin"),
    path("register/", views.register, name="BlogRegister"),
]
