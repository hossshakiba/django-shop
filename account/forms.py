from django import forms
from .models import User
import re

class SignupForm(forms.ModelForm):
    
    password1 = forms.CharField(widget= forms.PasswordInput())

    password2 = forms.CharField(widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data['email']
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError('ایمیل وارد شده تکراری است.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not bool(re.match('(0)?(9\d{9})', phone)) or len(phone) != 11:
            raise forms.ValidationError('شماره موبایل وارد شده غیر مجاز است.')

        phone_exists = User.objects.filter(phone=phone).exists()
        if phone_exists:
            raise forms.ValidationError('شماره موبایل وارد شده تکراری است.')
        return phone

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd['password1']
        password2 = cd['password2']
        if password1 != password2:
            raise forms.ValidationError('رمزهای عبور مغایرت دارند.')
        if len(password2) < 6:
            raise forms.ValidationError('حداقل طول رمز عبور ۶ است.')
        return cd

class LoginForm(forms.Form):
    email_or_phone  = forms.CharField(required=True)
    password        = forms.CharField(widget= forms.PasswordInput(), required=True)
    
    def __init__(self, request, *args, **kwargs):
        # simply do not pass 'request' to the parent
        super().__init__(*args, **kwargs)

class PersonalInfoForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(PersonalInfoForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "avatar")
        
        widgets = {
            'avatar': forms.FileInput()
        }


    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not bool(re.match('(0)?(9\d{9})', phone)) or len(phone) != 11:
    #         raise forms.ValidationError('شماره موبایل وارد شده غیر مجاز است.')

    #     phone_exists = User.objects.filter(phone=phone).exists()
    #     if phone_exists:
    #         raise forms.ValidationError('شماره موبایل وارد شده تکراری است.')
    #     return phone