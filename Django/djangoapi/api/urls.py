from django.urls import path
from .views import get_user, save_user, update_user

urlpatterns = [
    path('user/', get_user, name="get_users"),
    path('user/create', save_user, name="save_users"),
    path('user/<int:pk>', update_user, name="update_user"),
]