from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    items = Item.objects.category_sorted()

    return render(request, 'catalog/index.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'catalog/item.html', {'item': item})
