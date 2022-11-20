from django.test import Client, TestCase
from django.urls import reverse

from feedback.models import FeedBack


class FeedBackTest(TestCase):
    fixtures = ['fixtures/data.json', ]

    def test_feedback_form(self):
        feedbacks_count = FeedBack.objects.count()
        form_data = {
            'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing'
        }

        response = Client().post(reverse('feedback:feedback'),
                                 data=form_data,
                                 follow=True)

        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(FeedBack.objects.count(), feedbacks_count + 1,
                         'Object hasnt added')

        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertEqual(form['text'].help_text, 'Максимум: 1000 символов')
        self.assertEqual(form['text'].label, 'Текст обращения')
