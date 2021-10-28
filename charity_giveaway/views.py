from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from users.forms import LoginForm, RegisterForm
from charity_giveaway.models import Institution, Donation, Category
from django.db.models import Sum, Count
from users.models import CustomUser


# ---------- USER

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'charity_giveaway/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'charity_giveaway/register.html', {'form': form})
        else:
            return render(request, 'charity_giveaway/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'charity_giveaway/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                                           email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            return redirect('login')
        else:
            return render(request, 'charity_giveaway/register.html', {'form': form})


# ---------- PAGE

class LandingPageView(View):
    def get(self, request):
        bag = Donation.objects.all().aggregate(sum=Sum('quantity'))['sum']
        institution = Donation.objects.all().annotate(Count('institution', distinct=True))
        # institution = q[0].institution__count
        foundation = Institution.objects.filter(type=1).all()
        organisation = Institution.objects.filter(type=2).all()
        local = Institution.objects.filter(type=3).all()
        return render(request, 'charity_giveaway/index.html', {'bag': bag, 'institution': institution,
                                                               'foundation': foundation, 'organisation': organisation,
                                                               'local': local})


class AddDonationView(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'charity_giveaway/form.html', {'categories': categories, 'institutions': institutions})


class UserProfileView(View):
    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        donation = Donation.objects.filter(user_id=user_id)
        return render(request, 'charity_giveaway/profile.html', {'user': user, 'donation': donation})
