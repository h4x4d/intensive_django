from django.shortcuts import get_object_or_404
from datetime import date
from users.models import Account


def access_account(request):
    context = {}

    context['context_user'] = get_object_or_404(
        Account.objects.all().filter(is_active=True),
        pk=request.user.id
    ) if request.user.is_authenticated else None

    birthday_users = Account.objects.all().filter(
        is_active=True,
        birthday=date.today()
        ).only('id', 'email', 'first_name')
    context[
        'birthday_users'
        ] = birthday_users if birthday_users.first() else None
    return context
