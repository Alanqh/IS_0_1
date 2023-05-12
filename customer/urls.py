from django.urls import path
from customer.views import user_info, customer_home, change_password, service_records, service_application, \
    service_application_success

urlpatterns = [
    path('', customer_home, name='customer_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('service-records/', service_records, name='service_records'),
    path('service-application/', service_application, name='service_application'),
    path('service-application-success/',service_application_success, name='service_application_success'),
]
