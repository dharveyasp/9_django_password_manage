from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse, reverse_lazy

from . import forms
from .models import User


class Register(generic.CreateView):
    form_class = forms.RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    model = User


class Login(LoginView):
    model = User
    redirect_authenticated_user = True
    redirect_field_name = reverse_lazy('passwords_dashboard')
    template_name = 'users/login.html'
    next_page = reverse_lazy('passwords_dashboard')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "You are already logged in as %s " % self.request.user)
            return super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'Please enter the correct password!')
            return super().form_invalid(form)


class Logout(LogoutView):
    template_name = 'users/logout.html'
    redirect_field_name = reverse_lazy('login')
    next_page = reverse_lazy('login')
