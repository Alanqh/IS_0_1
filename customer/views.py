from .forms import UserInfoForm, ServiceApplicationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ChangePasswordForm
from .models import ServiceRecord


@login_required(login_url='login')
def customer_home(request):
    return render(request, 'customer_home.html')


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


# 在你的customer应用的views.py文件中


@login_required  # 限制只有登录用户才能访问该视图
def service_records(request):
    user = request.user  # 获取当前用户
    servicerecords = ServiceRecord.objects.filter(user_id=user.id)
    return render(request, 'service_records.html', {'service_records': servicerecords})


@login_required
def service_application(request):
    if request.method == 'POST':
        form = ServiceApplicationForm(request.POST)
        if form.is_valid():
            service_record = form.save(commit=False)
            service_record.user = request.user
            service_record.save()
            # 提交成功后，向售后服务部门发送订单记录的内容
            messages.success(request, '您的售后服务申请已提交成功！')
            return redirect('service_application_success')
    else:
        form = ServiceApplicationForm()
    return render(request, 'service_application.html', {'form': form})


def service_application_success(request):
    return render(request, 'service_application_success.html')
