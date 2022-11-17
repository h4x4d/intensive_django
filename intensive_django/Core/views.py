from django.shortcuts import render


def handler_404(request, exception):
    response = render(request, 'errors/404.html')
    response.status_code = 404

    return response
