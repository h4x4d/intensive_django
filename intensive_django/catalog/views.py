from django.shortcuts import render


def item_list(request):
    return render(request, 'catalog/index.html')


def item_detail(request, pk):
    return render(request, 'catalog/item.html', {'pk': pk})
