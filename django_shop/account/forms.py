from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "avatar")
        
        widgets = {
            'avatar': forms.FileInput()
        }
