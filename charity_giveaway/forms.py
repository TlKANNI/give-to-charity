import django.forms as forms
from django.forms import ModelForm
from django.core.validators import validate_email
from django.contrib.auth.forms import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first-name')
    last_name = forms.CharField(label='last-name')
    username = forms.EmailField(label='email', validators=[validate_email])
    email = forms.HiddenInput
    password = forms.CharField(label='pass1', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(label='pass2', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            raise forms.ValidationError("The password does not match!")
        return cleaned_data


