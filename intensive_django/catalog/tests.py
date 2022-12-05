from catalog.models import Category, Item, Tag
from django.core.exceptions import ValidationError
from django.test import Client, TestCase


class CatalogURLTests(TestCase):
    fixtures = ['fixtures/data.json']

    def test_catalog_default(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200,
                         f'Unexpected status code: {response.status_code}.'
                         f' Expected: {200}')

    def test_catalog_items(self):
        tests = (('3', 200), ('123', 404), ('asd', 404), ('0', 404),
                 ('1.123', 404), ('-123', 404))

        for i in tests:
            pk, status_code = i
            with self.subTest(pk=pk, status_code=status_code):
                response = Client().get(f'/catalog/{pk}/')
                self.assertEqual(response.status_code, status_code,
                                 f'Unexpected status code: '
                                 f'{response.status_code}.'
                                 f' Expected: {status_code}')


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
                             text='Random text',
                             )

            self.item.full_clean()
            self.item.save()

            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_to_create_with_need_word(self):
        item_count = Item.objects.count()

        self.item = Item(name='Test_item',
                         category=self.category,
                         text='Random text, but with "Роскошно"',
                         )

        self.item.full_clean()
        self.item.save()

        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)


class ContextTest(TestCase):
    fixtures = ['fixtures/data.json']

    def test_main_page_context(self):
        response = Client().get('/')

        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 4)
        self.assertEqual(list(response.context['page_obj']),
                         list(Item.objects.on_main()))

    def test_catalog_page_context_page_1(self):
        response = Client().get('/catalog/')

        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 5)
        self.assertEqual(list(response.context['page_obj']),
                         list(Item.objects.category_sorted()[:5]))

    def test_catalog_page_context_page_2(self):
        response = Client().get('/catalog/?page=2')

        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 1)
        self.assertEqual(list(response.context['page_obj']),
                         list(Item.objects.category_sorted()[5:]))

    def test_catalog_item_page_context(self):
        response = Client().get('/catalog/3/')

        self.assertIn('item', response.context)
        self.assertEqual(response.context['item'], Item.objects.get(pk=3))
