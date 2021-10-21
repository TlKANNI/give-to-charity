from django.shortcuts import render
from django.views import View
from charity_giveaway.forms import LoginForm, RegisterForm
from charity_giveaway.models import Institution, Donation
from django.db.models import Sum


class LandingPageView(View):
    def get(self, request):
        bag = Donation.objects.all().aggregate(sum=Sum('quantity'))['sum']
        institution = Institution.objects.count()
        inst_list = Institution.objects.first()
        return render(request, 'charity_giveaway/index.html', {'bag': bag, 'institution': institution,
                                                               'inst_list': inst_list})


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
