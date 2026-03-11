from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users),
    path('users/<int:user_id>', views.get_user_by_id),
    path('users/create', views.create_user),
    path('users/delete/<int:user_id>', views.delete_user)
]