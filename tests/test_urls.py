from django.test import SimpleTestCase
from django.urls import resolve, reverse
from pages.views import *
from payments.views import *

class PagesUrlTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_gallery_status_code(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)

    def test_gallery_url_is_resolved(self):
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, gallery)

    def test_contact_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_booking_status_code(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)

    def test_booking_url_is_resolved(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func, booking)

class PaymentsUrlTests(SimpleTestCase):
    def test_payment_success_status_code(self):
        response = self.client.get('/success/')
        self.assertEqual(response.status_code, 200)

    def test_payment_success_is_resolved(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, payment_success)

    def test_payment_failed_status_code(self):
        response = self.client.get('/failed/')
        self.assertEqual(response.status_code, 200)

    def test_payment_failed_is_resolved(self):
        url = reverse('failed')
        self.assertEquals(resolve(url).func, payment_failed)