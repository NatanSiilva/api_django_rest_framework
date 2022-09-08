from django.urls import path
from apps.users.api import api

urlpatterns = [
    # path('users/', api.UserAPIView.as_view(), name='api_users'),
    path('users/', api.user_api_view, name='api_users'),
    path('users/<int:pk>/', api.user_detail_api_view, name='api_users_detail'),
]
