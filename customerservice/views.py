from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages

from customer.forms import UserInfoForm, ChangePasswordForm
from customer.models import ServiceRecord
from inventory.models import InventoryProducts, ProductList
from register.models import User


@login_required(login_url='login')
def customerservice_home(request):
    return render(request, 'customer-service_home.html')




@login_required  # 限制只有登录用户才能访问该视图
def service_records(request):
    servicerecords = ServiceRecord.objects.all
    return render(request, 'service_records.html', {'service_records': servicerecords})

@login_required
def customer_information(request):
    customers = User.objects.filter(role='customer')
    for customer in customers:
        if customer.gender == 'male':
            customer.gender = '男'
        else :
            customer.gender = '女'
    return render(request, 'customer_information.html', {'customers': customers})