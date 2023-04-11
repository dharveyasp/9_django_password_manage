from django import forms
from .models import Password


class EditForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = ("title", "user_name", "pass_word", "description")
