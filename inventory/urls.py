from django.urls import path
from customer.views import user_info, change_password
from customerservice.views import service_records
from inventory.views import inventory_home, purchase_product, purchase_success, inventory_list, inventory_change_list

urlpatterns = [
    path('', inventory_home, name='inventory_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('purchase_product/', purchase_product, name='purchase_product'),
    path('purchase_success/', purchase_success, name='purchase_success'),
    path('inventory_list/', inventory_list, name='inventory_list'),
    path('inventory_change_list/', inventory_change_list, name='inventory_change_list'),
    path('service_records/',service_records, name='service_records'),

]