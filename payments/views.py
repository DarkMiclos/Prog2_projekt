from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import stripe

@csrf_exempt
def create_checkout_session(request, id):
    pass

def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failed(request):
    return render(request, 'payments/payment_failed.html')

def order_history():
    pass