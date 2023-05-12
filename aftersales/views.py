from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages

from customer.forms import UserInfoForm, ChangePasswordForm


@login_required(login_url='login')
def aftersales_home(request):
    return render(request, 'aftersales_home.html')

