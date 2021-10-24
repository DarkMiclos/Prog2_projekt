from django.shortcuts import render
from django.http import HttpResponse

from payments.models import Product

def home(request):
    return render(request, "layouts/home.html", {})

def gallery(request):
    return render(request, "layouts/gallery.html")

def contact(request):
    return render(request, "layouts/contact.html")

def booking(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, "layouts/booking.html", data)