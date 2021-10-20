from django.shortcuts import render
from django.views import View
from charity_giveaway.forms import LoginForm, RegisterForm


class LandingPageView(View):
    def get(self, request):
        return render(request, 'charity_giveaway/index.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity_giveaway/form.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'charity_giveaway/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'charity_giveaway/register.html', {'form': form})
