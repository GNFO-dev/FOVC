"from django.test import TestCase

# Create your tests here.
"
from django.test import TestCase

class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.post('/login/', {'username': 'admin', 'password': '1234'})
        self.assertEqual(response.status_code, 200)
