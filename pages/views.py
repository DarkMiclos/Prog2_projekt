from django.shortcuts import render
from django.http import HttpResponse
from pages.forms import BookingForm
from payments.views import coinbase_commerce_payment

from .models import Event, Image
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
    booking_form = BookingForm()
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            Event.objects.create(**booking_form.cleaned_data)
        else:
            print(booking_form.errors)
    data = {
        'products': products,
        'charge': charge,
        'booking_form': booking_form,
    }
    return render(request, "layouts/booking.html", data)