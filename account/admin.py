from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'phone', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'first_name', 'last_name', 'avatar')}),
        ('رمز عبور', {'fields': ('password',)}),
        ('دسترسی‌ها', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'phone', 'first_name', 'last_name', 'avatar')}),
        ('رمز عبور', {'fields': ('password1', 'password2')}),
        ('دسترسی‌ها', {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email', 'phone')
    ordering = ('email',)


admin.site.register(User, UserAdmin)