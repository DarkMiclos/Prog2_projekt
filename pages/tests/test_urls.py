from django.http import response
from django.test import TestCase

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_gallery(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_booking(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)