from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout


class Login(LoginView):
    template_name = 'accounts/login.html'


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
