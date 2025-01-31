from django.urls import path
from . import views


urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
    path('users/create/', views.user_create, name='user_create'),
]

