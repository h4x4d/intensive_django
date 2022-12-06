from catalog.views import ItemDetailView, ItemListView
from django.urls import path, re_path

app_name = 'catalog'

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    re_path(r'(?P<pk>[1-9][0-9]*)/$', ItemDetailView.as_view(),
            name='item_detail'),
]
