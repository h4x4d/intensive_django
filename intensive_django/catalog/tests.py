from django.test import TestCase, Client


class CatalogURLTests(TestCase):
    def test_catalog_default(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200,
                         f"Unexpected status code: {response.status_code}."
                         f" Expected: {200}")

    def test_catalog_items(self):
        tests = (("123", 200), ("asd", 404), ("0", 404),
                 ("1.123", 404), ("-123", 404))

        for i in tests:
            pk, status_code = i
            with self.subTest(pk=pk, status_code=status_code):
                response = Client().get(f"/catalog/{pk}/")
                self.assertEqual(response.status_code, status_code,
                                 f"Unexpected status code: "
                                 f"{response.status_code}."
                                 f" Expected: {status_code}")
