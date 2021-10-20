import django.forms as forms
from django.forms import ModelForm
from django.core.validators import validate_email


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.CharField(label='',
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Example@mail.com'}),
                            validators=[validate_email])
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password_repeat = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'repeat password'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            raise forms.ValidationError("The password does not match!")
        return cleaned_data
