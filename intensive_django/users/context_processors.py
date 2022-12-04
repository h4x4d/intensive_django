from django.shortcuts import get_object_or_404

from .models import Account


def access_account(request):
    if request.user.is_authenticated:
        return {'context_user': get_object_or_404(
            Account.objects.all().filter(is_active=True),
            pk=request.user.id
        )}
    return {'context_user': None}
