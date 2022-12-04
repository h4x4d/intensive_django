from django.views.generic import TemplateView


class NotFoundView(TemplateView):
    template_name = 'errors/404.html'
    status_code = 404
