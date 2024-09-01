from django.test import TestCase
from django.urls import reverse

class SimpleTests(TestCase):

    def test_index_view(self):
        # Ensure the URL name matches what is in your `urls.py`
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/index.html')
