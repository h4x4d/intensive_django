from catalog.models import Item
from django.views.generic import ListView


class HomepageView(ListView):
    paginate_by = 5
    model = Item
    queryset = Item.objects.on_main()

    template_name = 'homepage/index.html'
