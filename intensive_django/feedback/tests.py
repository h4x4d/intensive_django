from django.test import Client, TestCase
from django.urls import reverse

from feedback.models import FeedBack


class FeedBackTest(TestCase):
    fixtures = ['fixtures/data.json', ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        form_data = {
            'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing'
        }

        cls.feedbacks_count = FeedBack.objects.count()

        cls.response = Client().post(reverse('feedback:feedback'),
                                     data=form_data,
                                     follow=True)

    @property
    def form(self):
        self.assertIn('form', self.response.context)
        form = self.response.context['form']

        return form

    def test_feedbacks_len(self):
        self.assertEqual(FeedBack.objects.count(), self.feedbacks_count + 1,
                         'Object hasnt added')

    def test_redirect(self):
        self.assertRedirects(self.response, reverse('feedback:feedback'))

    def test_response_context_label(self):
        self.assertEqual(self.form['text'].label, 'Текст обращения')

    def test_response_context_help_text(self):
        self.assertEqual(self.form['text'].help_text,
                         'Максимум: 1000 символов')
