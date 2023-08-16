from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm as UsercСreationFormDjango
)
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AuthenticationAjaxForm(forms.Form):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "autocorret", 'class': 'form-control'})

    )
    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "off", 'class': 'form-control'})
    )




class RegistAjaxForm(forms.Form):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": 'email', 'class': 'form-control'})
    )
    nickname= forms.CharField(
        label= ("nickname"),
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "off", 'class': 'form-control'})
    )

    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'})
    )
class ResetAjaxForm(forms.Form):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "off", 'class': 'form-control'})
    )


class UserCreationForm(UsercСreationFormDjango):
    email=forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UsercСreationFormDjango.Meta):
        model=User
        fields=("username", "email")