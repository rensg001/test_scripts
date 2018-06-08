from django.test import TestCase
from django.core.urlresolvers import reverse_lazy

from .models import RestTest

# Create your tests here.


class RestTestCase(TestCase):

    def setUp(self):
        t = RestTest(**{"name": "xxx"})
        t.save()

    def test_rest(self):
        url = reverse_lazy('rest_v1:bad')
        response = self.client.get(url)
        print(response.content)