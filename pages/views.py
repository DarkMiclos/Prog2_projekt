from django.shortcuts import render
from django.http import HttpResponse
from payments.views import coinbase_commerce_payment

from .models import Image
from payments.models import Product

def home(request):
    return render(request, "layouts/home.html")

def gallery(request):
    images = Image.objects.all()
    data = {
        'images': images
    }
    return render(request, "layouts/gallery.html", data)

def contact(request):
    return render(request, "layouts/contact.html")

def booking(request):
    products = Product.objects.all()
    charge = coinbase_commerce_payment(request)
    data = {
        'products': products,
        'charge': charge
    }
    return render(request, "layouts/booking.html", data)