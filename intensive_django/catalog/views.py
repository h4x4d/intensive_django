from catalog.models import Item
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, ListView
from rating.forms import SetRatingForm
from rating.models import Rating


class ItemListView(ListView):
    paginate_by = 5
    model = Item
    queryset = Item.objects.category_sorted()

    template_name = 'catalog/index.html'


class ItemDetailView(DetailView, FormView):
    model = Item
    template_name = 'catalog/item.html'
    form_class = SetRatingForm

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        item = get_object_or_404(Item, pk=pk)

        try:
            rating = Rating.objects.get_rating_from_user(
                item.id, request.user.id).rating
        except Rating.DoesNotExist:
            rating = 0

        form = SetRatingForm(request.POST or None, initial={
            'rating': rating,
        })

        item_ratings = Rating.objects.filter_by_item(item.id)

        rating_count = item_ratings.count()

        avg_rating = item_ratings.aggregate(Avg('rating'))['rating__avg']

        context = {
            'item': item,
            'form': form,
            'rating_count': rating_count,
            'avg_rating': avg_rating,
        }

        return render(request, self.template_name, context)

    def form_valid(self, form):
        if form.is_valid():
            pk = self.kwargs['pk']
            item = get_object_or_404(Item, pk=pk)
            form.save(self.request.user, item)

            return redirect('catalog:item_detail', pk=pk)
