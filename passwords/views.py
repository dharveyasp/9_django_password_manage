from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


class Dashboard(generic.TemplateView):
    template_name = 'passwords/dashboard.html'
