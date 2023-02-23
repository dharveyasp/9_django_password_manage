from django.shortcuts import render
from django.views import generic


class Dashboard(generic.TemplateView):
    template_name = 'passwords/dashboard.html'
