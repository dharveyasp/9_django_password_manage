from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from parsley.decorators import parsleyfy

non_allowed_usernames = ['abc', '123']


@parsleyfy
class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@parsleyfy
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
