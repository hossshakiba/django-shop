from django.urls import path
from .views import (
    Register,
    login_view
)

app_name = 'account'
urlpatterns = [
    path('sign-up', Register.as_view(), name='sign-up'),
    path('login', login_view, name='login')
]
