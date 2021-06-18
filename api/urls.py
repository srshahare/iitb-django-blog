from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('token', obtain_auth_token, name="api_token"),
    path('create', views.CreateApi.as_view(), name="create_blog"),
    path('delete', views.DeleteApi.as_view(), name="delete_blog"),
    path('update', views.UpdateApi.as_view(), name="update_blog"),
    path('list', views.ListApi.as_view(), name="list_blogs"),
]
