from django.test import TestCase
from django.test import Client

# Create your tests here.
from django.urls import reverse_lazy


class IndexTestCase(TestCase):

    def test_index_view(self):
        client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        url = reverse_lazy('index')
        resp = client.get(url)
        self.assertTrue(resp.status_code == 200)