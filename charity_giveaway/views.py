from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from charity_giveaway.forms import LoginForm, RegisterForm
from charity_giveaway.models import Institution, Donation
from django.db.models import Sum
from django.contrib.auth.models import User


class LandingPageView(View):
    def get(self, request):
        bag = Donation.objects.all().aggregate(sum=Sum('quantity'))['sum']
        institution = Institution.objects.count()
        foundation = Institution.objects.filter(type=1).all()
        organisation = Institution.objects.filter(type=2).all()
        local = Institution.objects.filter(type=3).all()
        return render(request, 'charity_giveaway/index.html', {'bag': bag, 'institution': institution,
                                                               'foundation': foundation, 'organisation': organisation,
                                                               'local': local})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity_giveaway/form.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'charity_giveaway/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'charity_giveaway/login.html', {'form': form})
        else:
            return render(request, 'charity_giveaway/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'charity_giveaway/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                                     username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            return redirect('login')
        else:
            return render(request, 'charity_giveaway/register.html', {'form': form})
