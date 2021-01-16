import re
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignupForm
from django.views.generic import (
    View,
    ListView,
	CreateView,
	UpdateView,
	DeleteView)
from .models import User

class Register(CreateView):
	form_class 		= SignupForm
	template_name 	= "account/signup.html"

	def form_valid(self, form):
		form.save()
		return redirect('/')

