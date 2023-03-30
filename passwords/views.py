from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import User, Password


class Dashboard(generic.ListView):
    template_name = 'passwords/dashboard.html'
    model = Password
