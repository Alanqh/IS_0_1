from django.urls import path

from customerservice.views import user_info, change_password, customerservice_home, service_records

urlpatterns = [
    path('', customerservice_home, name='customerservice_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('service_records/', service_records, name='service_records'),
]