from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .forms import EditForm
from .models import User, Password


class AuthUser:
    def get_queryset(self):
        qs = Password.objects.filter(user=self.request.user)
        return qs


class Dashboard(AuthUser, generic.ListView):
    template_name = 'passwords/dashboard.html'
    model = Password


class Detail(AuthUser, generic.DetailView):
    model = Password
    template_name = 'passwords/detail.html'


class Edit(AuthUser, generic.UpdateView):
    model = Password
    template_name = 'passwords/edit.html'
    form_class = EditForm

    def get_success_url(self):
        return reverse_lazy('passwords_detail', kwargs={'pk': self.object.id})


class Create(AuthUser, generic.CreateView):
    model = Password
    template_name = 'passwords/create.html'
    form_class = EditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('passwords_detail', kwargs={'pk': self.object.id})


class Delete(AuthUser, generic.DeleteView):
    model = Password
    template_name = 'passwords/password_confirm_delete.html'
    success_url = reverse_lazy('passwords_dashboard')
