from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.contrib import messages
from customer.forms import UserInfoForm, ChangePasswordForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductList, InventoryProducts, PurchaseOrder, InventoryChange
from .forms import PurchaseForm


@login_required(login_url='login')
def inventory_home(request):
    return render(request, 'inventory_home.html')


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


@login_required
def purchase_product(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            if quantity <= 0:
                messages.error(request, '购买数量必须大于0')
                return redirect('purchase')

            # 创建新的采购订单
            purchase_order = PurchaseOrder.objects.create(
                product=product,
                quantity=quantity
            )

            # 更新库存产品表中对应产品的数量
            inventory_product, created = InventoryProducts.objects.get_or_create(
                product=product
            )
            inventory_product.quantity += quantity
            inventory_product.save()

            # 更新库存变化表
            inventory_change = InventoryChange.objects.create(
                product=product,
                change_amount=quantity,
                description=f"Purchased {quantity} {product.name}"
            )

            messages.success(request, '采购成功')
            return redirect('purchase_success')
    else:
        form = PurchaseForm()

    products = ProductList.objects.all()
    context = {'form': form, 'products': products}
    return render(request, 'purchase_product.html', context)



@login_required
def purchase_success(request):
    return render(request, 'purchase_success.html')
