from django.test import TestCase , SimpleTestCase

# Create your tests here.
class Tests(SimpleTestCase):
    def testhome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def testmp(self):
        response = self.client.get('/tmp/')
        self.assertEqual(response.status_code,200)