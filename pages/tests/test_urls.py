from django.test import TestCase

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_gallery(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)