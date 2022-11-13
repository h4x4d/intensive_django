from django.shortcuts import render

from catalog.models import Item


def home(request):
    items = Item.objects.on_main()

    context = {
        'items': items
    }

    return render(request, 'homepage/index.html', context=context)
