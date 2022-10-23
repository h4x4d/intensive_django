from django.http import HttpResponse


def item_list(request):
    return HttpResponse("Список элементов")


def item_detail(request, primary_key):
    return HttpResponse(f"Подробно элемент №{primary_key}")
