from django.urls import path


from aftersales.views import aftersales_home, user_info, change_password

urlpatterns = [
    path('', aftersales_home, name='aftersales_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
]