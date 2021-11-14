from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.conf import settings
from .models import *
import stripe
from coinbase_commerce.client import Client

booking_product = Product.objects.get(id = 1)

@csrf_exempt
def stripe_config(request):
    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [
            {
                'price_data': {
                    'currency': 'huf',
                    'product_data': {
                    'name': booking_product.name,
                    },
                    'unit_amount': int(booking_product.price) * 100,
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

def coinbase_commerce_payment(request):
    client = Client(api_key = settings.COINBASE_COMMERCE_API_KEY)
    success_url = request.build_absolute_uri(reverse('success'))
    cancel_url = request.build_absolute_uri(reverse('failed'))
    product = {
        'name': booking_product.name,
        'description': booking_product.description,
        'local_price': {
            'amount': booking_product.price,
            'currency': 'HUF'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': success_url,
        'cancel_url': cancel_url,
    }
    charge = client.charge.create(**product)

    return charge