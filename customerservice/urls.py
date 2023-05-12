from django.urls import path
from customer.views import user_info, change_password
from customerservice.views import customerservice_home, customer_information, service_records
from inventory.views import inventory_list

urlpatterns = [
    path('', customerservice_home, name='customerservice_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('service_records/', service_records, name='service_records'),
    path('inventory_list/', inventory_list, name='inventory_list'),
    path('customer_information/', customer_information, name='customer_information')
]