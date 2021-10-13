from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {})

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def booking(request):
    return render(request, "booking.html")