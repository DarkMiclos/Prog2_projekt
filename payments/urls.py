from django.urls import path
from .views import *

urlpatterns = [
    path('success/', payment_success, name = 'success'),
    path('failed/', payment_failed, name = 'failed'),
    path('config/', stripe_config, name = 'config'),
    path('create-checkout-session/', create_checkout_session, name = 'create_checkout_session'),
]