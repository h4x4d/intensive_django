from django.urls import path, re_path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    re_path(r'(?P<pk>[1-9][0-9]*)/$', views.ItemDetailView.as_view(),
            name='item_detail'),
]
