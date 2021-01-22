from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	DetailView,
	CreateView,
	UpdateView )
from .models import User
from .forms import SignupForm, PersonalInfoForm

class Register(CreateView):
	form_class 		= SignupForm
	template_name 	= "registration/signup.html"
	success_url		= reverse_lazy('account:login')

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/')
		return super().get(request)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password1'])
		user.save()
		return super().form_valid(form)

class Login(LoginView):
	template_name 	= "registration/login.html"

	def get_success_url(self):
		return reverse_lazy('home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


class ProfilePersonalInfo(LoginRequiredMixin, UpdateView, DetailView):
	model 			= User
	form_class 	  	= PersonalInfoForm
	template_name 	= "registration/profile_personal_info.html"
	success_url   	= reverse_lazy("account:profile")

	def get_object(self):
		return self.request.user