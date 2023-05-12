from django.urls import path


from inventory.views import inventory_home, user_info, change_password, purchase_product, purchase_success


urlpatterns = [
    path('', inventory_home, name='inventory_home'),
    path('user_info/', user_info, name='user_info'),
    path('change_password/', change_password, name='change_password'),
    path('purchase_product/', purchase_product, name='purchase_product'),
    path('purchase_success/', purchase_success, name='purchase_success'),

]