from django.urls import path, re_path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name="catalog-items-summary"),
    re_path(r'(?P<pk>^[1-9][0-9]*)/$', views.item_detail,
            name="catalog-item-detail")
]
