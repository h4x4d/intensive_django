from django.test import TestCase, Client


class HomepageURLTests(TestCase):
    def test_homepage(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {200}")
