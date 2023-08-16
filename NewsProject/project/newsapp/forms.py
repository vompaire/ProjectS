from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from .models import New, NewsOut


# class CustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields.pop('password2')

class NewFormOut(forms.ModelForm):
    class Meta:
        model = NewsOut
        fields = ['title', 'link', 'image']


class NewForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = New
        fields = ['name', 'description', 'category']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
