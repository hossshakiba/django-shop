import re
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views.generic.detail import DetailView
from .forms import SignupForm, LoginForm, PersonalInfoForm
from django.contrib import messages
from django.views.generic import (
    ListView,
	CreateView,
	UpdateView,
	DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

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


def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	
	form = LoginForm(request.POST or None)
	if form.is_valid():
		cd = form.cleaned_data
		try:
			user = authenticate(request, email=User.objects.get(phone=cd['email_or_phone']), password=cd['password'])
		except:
			user = authenticate(request, email=cd['email_or_phone'], password=cd['password'])
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.error(request, 'کاربری با مشخصات وارد شده یافت نشد!')

	return render(request, "registration/login.html", {'form':form})


def logout_view(request):
    logout(request)
    return redirect('/login')


class ProfilePersonalInfo(LoginRequiredMixin, UpdateView, DetailView):
	model 			= User
	form_class 	  	= PersonalInfoForm
	template_name 	= "registration/profile_personal_info.html"
	success_url   	= reverse_lazy("account:profile")

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

	def get_object(self):
		return self.request.user