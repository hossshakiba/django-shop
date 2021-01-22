from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
    Register,
    Login,
    logout_view,
    ProfilePersonalInfo
)

app_name = 'account'
urlpatterns = [
    path('sign-up', Register.as_view(), name= 'sign-up'),
    path('login', Login.as_view(), name= 'login'),
    path('logout', logout_view, name= 'logout'),
    path('profile', ProfilePersonalInfo.as_view(), name= 'profile'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url = reverse_lazy('account:password_reset_done')), name= 'password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        success_url = reverse_lazy('account:password_reset_complete')), name= 'password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        success_url= reverse_lazy('account:password_change_done')), name= 'password_change'),

    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name= 'password_change_done'),
]
