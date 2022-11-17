from django.core.paginator import Paginator
from django.shortcuts import render

from catalog.models import Item


def home(request):
    items = Item.objects.on_main()

    paginator = Paginator(items, 5)
    page_number = request.GET.get('page', 1)

    page_obj = paginator.get_page(page_number)
    return render(request, 'homepage/index.html', {'page_obj': page_obj})
