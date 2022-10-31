from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from .models import Category, Item, Tag


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


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(is_published=True,
                                               name='Test Category',
                                               slug='category_1',
                                               weight=100)

        cls.tag = Tag.objects.create(is_published=True,
                                     name='Test tag',
                                     slug='tag_1')

    def test_unable_to_create_with_no_word(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(name='Test_item',
                             category=self.category,
                             text="Random text",
                             )

            self.item.full_clean()
            self.item.save()

            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_to_create_with_need_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test_item',
                         category=self.category,
                         text="Random text, but with 'Роскошно'",
                         )

        self.item.full_clean()
        self.item.save()

        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)
