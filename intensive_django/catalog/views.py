from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from catalog.models import Item


class ItemListView(ListView):
    paginate_by = 5
    model = Item
    queryset = Item.objects.category_sorted()

    template_name = 'catalog/index.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'catalog/item.html'


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'catalog/item.html', {'item': item})
