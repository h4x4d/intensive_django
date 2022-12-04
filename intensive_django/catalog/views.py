from catalog.models import Item
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from rating.forms import SetRatingForm
from rating.models import Rating


def item_list(request):
    items = Item.objects.category_sorted()

    paginator = Paginator(items, 5)
    page_number = request.GET.get('page', 1)

    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/index.html', {'page_obj': page_obj})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # <----------- pulling item rating from user ------------->
    rating = 0
    try:
        rating = Rating.objects.get_rating_from_user().rating
    except Exception:
        pass

    # <--------- creating form --------->
    form = SetRatingForm(request.POST or None, initial={
        'rating': rating
    })

    if request.method == 'POST' and form.is_valid():
        form.save(request.user, item)

        redirect('catalog:item_detail', pk=item.id)

    item_ratings = Rating.objects.filter_by_item(item.id)

    rating_count = item_ratings.count()

    # <----------- calculating average rating for the item -------------->
    avg_rating = 0.0
    try:
        avg_rating = sum(r.rating for r in item_ratings) / rating_count
    except Exception:
        pass

    context = {
        'item': item,
        'form': form,
        'button_name': 'Поставить',
        'form_method': 'POST',
        'rating_count': rating_count,
        'avg_rating': avg_rating
    }

    return render(request, 'catalog/item.html', context)
