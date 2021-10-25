from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.conf import settings
from stripe.api_resources import customer, line_item, payment_method, product
from .models import *
import stripe
import json

@csrf_exempt
def stripe_config(request):
    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    product = Product.objects.all()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [
            {
                'price_data': {
                    'currency': 'huf',
                    'product_data': {
                    'name': 'Foglalás',
                    },
                    'unit_amount': '30000',
                },
                
                'quantity': 1,

            }
        ],
        mode = 'payment',
        success_url = request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )
    return JsonResponse({'sessionId': checkout_session.id})

def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failed(request):
    return render(request, 'payments/payment_failed.html')

def order_history():
    pass