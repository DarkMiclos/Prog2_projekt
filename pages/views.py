from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "layouts/home.html", {})

def gallery(request):
    return render(request, "layouts/gallery.html")

def contact(request):
    return render(request, "layouts/contact.html")

def booking(request):
    return render(request, "layouts/booking.html")