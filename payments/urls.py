from django.urls import path
from .views import *

urlpatterns = [
    path('success/', payment_success, name = 'success'),
    path('failed/', payment_failed, name = 'failed'),

    path('api/checkout-session/<id>/', create_checkout_session, name = 'api_checkout_session'),
]