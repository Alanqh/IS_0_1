from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages

from customer.forms import UserInfoForm, ChangePasswordForm
from customer.models import ServiceRecord


@login_required(login_url='login')
def customerservice_home(request):
    return render(request, 'customer-service_home.html')


@login_required(login_url='login')
def user_info(request):
    user = request.user
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
    else:
        form = UserInfoForm(instance=user)
    return render(request, 'user_info.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '密码已成功修改！')
            return redirect('index_login')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required  # 限制只有登录用户才能访问该视图
def service_records(request):
    servicerecords = ServiceRecord.objects.all
    return render(request, 'service_records.html', {'service_records': servicerecords})
