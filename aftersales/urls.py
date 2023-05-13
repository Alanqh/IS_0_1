from django.urls import path
from aftersales.views import aftersales_home, uncompleted_orders, process_order
from customer.views import user_info, change_password
from inventory.views import inventory_list

urlpatterns = [
    path('', aftersales_home, name='aftersales_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('uncompleted-orders/', uncompleted_orders, name='uncompleted_orders'),
    path('process-order/<int:order_id>/', process_order, name='process_order'),
    path('inventory_list/', inventory_list, name='inventory_list'),
]