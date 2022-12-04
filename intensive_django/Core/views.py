from django.views.generic import TemplateView


class NotFoundView(TemplateView):
    template_name = 'errors/404.html'

    def get(self, request, *args, **kwargs):
        response = super(NotFoundView, self).get(request, *args, **kwargs)
        response.status_code = 404

        return response
