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
    rating = 0
    try:
        rating = Rating.objects.get(account_id=request.user.id,
                                    item_id=item.id).rating
    except Exception:
        pass

    rating_count = Rating.objects.filter(item_id=item.id).count()
    avg_rating = sum(r.rating for r in Rating.objects.filter(
        item_id=item.id)) / rating_count

    form = SetRatingForm(request.POST or None, initial={
        'rating': rating
    })
    context = {
        'item': item,
        'form': form,
        'button_name': 'Поставить',
        'form_method': 'POST',
        'rating_count': rating_count,
        'avg_rating': avg_rating
    }

    if request.method == 'POST' and form.is_valid():
        form.save(request.user, item)

        redirect('catalog:item_detail', pk=item.id)

    return render(request, 'catalog/item.html', context)
