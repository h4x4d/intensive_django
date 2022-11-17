from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    items = Item.objects.category_sorted()

    paginator = Paginator(items, 5)
    page_number = request.GET.get('page', 1)

    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/index.html', {'page_obj': page_obj})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'catalog/item.html', {'item': item})
