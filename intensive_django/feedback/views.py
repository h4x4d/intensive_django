from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from feedback.forms import FeedBackForm
from feedback.models import FeedBack
from intensive_django.settings import FROM_MAIL, TO_MAIL


class FeedbackFormView(FormView):
    template_name = 'feedback/index.html'
    form_class = FeedBackForm
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
        FeedBack.objects.create(**form.cleaned_data)

        send_mail(
                  'Новая обратная связь по форме',
                  f'{form.cleaned_data.get("text")}',
                  FROM_MAIL,
                  TO_MAIL,
                  fail_silently=True,
        )

        return super().form_valid(form)
