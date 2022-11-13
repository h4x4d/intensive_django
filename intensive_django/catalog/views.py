from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    items = Item.objects.category_sorted()

    return render(request, 'catalog/index.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=int(pk))

    return render(request, 'catalog/item.html', {'item': item})
