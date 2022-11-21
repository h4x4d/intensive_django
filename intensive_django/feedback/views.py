import os

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from feedback.forms import FeedBackForm
from feedback.models import FeedBack


def feedback(request):

    form = FeedBackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        FeedBack.objects.create(
            **form.cleaned_data
        )

        send_mail(
            'Новая обратная связь по форме',
            f'{form.cleaned_data.get("text")}',
            os.getenv('FROM_MAIL', ''),
            (os.getenv('TO_MAIL', '').split(';'),),
            fail_silently=True
        )

        return redirect('feedback:feedback')

    return render(request, 'feedback/index.html', context)
