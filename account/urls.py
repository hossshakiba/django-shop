from django.urls import path
from .views import (
    Register,
)

urlpatterns = [
    path('sign-up', Register.as_view(), name='sign-up')
]
