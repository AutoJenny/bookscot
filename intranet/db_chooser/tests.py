from django.test import TestCase
from django.urls import reverse

class FetchDataTestCase(TestCase):
    def test_fetch_data(self):
        # Assuming 'YourModelName' is a valid model in your 'db_chooser' app
        # and it has at least one instance with id=1
        url = reverse('fetch_data') + '?table=aibos_site_article&columns=title&columns=title&row_id=3'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Further checks can include verifying the structure of the response data
