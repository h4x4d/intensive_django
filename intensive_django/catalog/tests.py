from django.test import TestCase, Client


class CatalogURLTests(TestCase):
    def test_catalog_default(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {200}")

    def test_catalog_good(self):
        response = Client().get("/catalog/123")
        self.assertEqual(response.status_code, 200,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {200}")

    def test_catalog_bad_string(self):
        response = Client().get("/catalog/asd")
        self.assertEqual(response.status_code, 404,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {404}")

    def test_catalog_bad_zero(self):
        response = Client().get("/catalog/0")
        self.assertEqual(response.status_code, 404,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {404}")

    def test_catalog_bad_decimal(self):
        response = Client().get("/catalog/1.5")
        self.assertEqual(response.status_code, 404,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {404}")

    def test_catalog_bad_less_than_zero(self):
        response = Client().get("/catalog/-11")
        self.assertEqual(response.status_code, 404,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {404}")
