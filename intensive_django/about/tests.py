from django.test import Client, TestCase


class AboutURLTests(TestCase):
    def test_about(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200,
                         f'Unexpected status code: {response.status_code}.'
                         f' Expected: {200}')
