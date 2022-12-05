from catalog.models import Item
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

    def get(self, request, pk):
        self.item = get_object_or_404(Item, pk=self.kwargs['pk'])
        self.user = request.user

        # <----------- pulling item rating from user ------------->
        rating = 0
        try:    # try to get existing rating
            rating = Rating.objects.get_rating_from_user(
                self.item.id, request.user.id).rating
        except Rating.DoesNotExist:  # ignore if no rating
            pass

        # <--------- creating form --------->
        self.form = SetRatingForm(request.POST or None, initial={
            'rating': rating
        })

        item_ratings = Rating.objects.filter_by_item(self.item.id)

        rating_count = item_ratings.count()

        # <----------- calculating average rating for the item -------------->
        avg_rating = 0.0
        try:    # try to calculate average
            avg_rating = sum(r.rating for r in item_ratings) / rating_count
        except ZeroDivisionError:   # ingore if no ratings (rating_count == 0)
            pass

        context = {
            'item': self.item,
            'form': self.form,
            'rating_count': rating_count,
            'avg_rating': avg_rating
        }

        return render(request, self.template_name, context)

    def form_valid(self, form):
        if form.is_valid():
            pk = self.kwargs['pk']
            item = get_object_or_404(Item, pk=pk)
            form.save(self.request.user, item)

            return redirect('catalog:item_detail', pk=pk)
