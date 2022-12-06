from users.models import Account
from django.test import Client, TestCase
from django.urls import reverse
from datetime import date


class TestContextProcessor(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.User = Account.objects.create(
            email='user@example.com',
            birthday=date.today(),
        )
        cls.User.set_password('test-password')
        cls.User2 = Account.objects.create(
            email='user2@example.com',
            password='test-password',
        )
        cls.User.save()
        cls.User2.save()

    def test_birthday(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('birthday_users', response.context)
        self.assertEqual(len(response.context['birthday_users']), 1)

    def test_user_authenticated(self):
        client = Client()
        client.login(username=self.User.email, password='test-password')
        response = client.get(reverse('homepage:home'))
        self.assertIn('context_user', response.context)
        self.assertEqual(
            response.context['context_user'].email,
            'user@example.com'
        )

    def test_user_not_authenticated(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.context['context_user'], None)
