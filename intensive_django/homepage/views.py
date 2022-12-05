from django.views.generic import ListView

from catalog.models import Item


class HomepageView(ListView):
    paginate_by = 5
    model = Item
    queryset = Item.objects.on_main()

    template_name = 'homepage/index.html'
