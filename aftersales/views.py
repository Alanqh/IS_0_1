from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from customer.models import ServiceRecord


@login_required(login_url='login')
def aftersales_home(request):
    return render(request, 'aftersales_home.html')


@login_required(login_url='login')
def uncompleted_orders(request):
    orders = ServiceRecord.objects.filter(service_state=0)
    return render(request, 'uncompleted_orders.html', {'orders': orders})


@login_required(login_url='login')
def process_order(request, order_id):
    order = ServiceRecord.objects.get(id=order_id)

    if request.method == 'POST':
        # 处理订单逻辑
        order.service_state = 1
        order.save()
        return redirect('uncompleted_orders')

    return render(request, 'process_order.html', {'order': order})