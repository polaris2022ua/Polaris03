from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), max_length=100, widget=forms.EmailInput(attrs={"autocomplete": "email"}))
    username = forms.CharField(label=_("Username"), max_length=40, )
    phone = forms.CharField(label=_("Phone"), max_length=15, )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone")
