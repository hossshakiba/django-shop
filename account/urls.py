from django.contrib.auth import logout
from django.urls import path
from .views import (
    Register,
    login,
    logout,
)

app_name = 'account'
urlpatterns = [
    path('sign-up', Register.as_view(), name='sign-up'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]
