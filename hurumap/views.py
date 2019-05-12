from django.views.generic import TemplateView
from django.conf import settings


class EmbedView(TemplateView):
    template_name = "embed/iframe.html"

    def get_context_data(self, **kwargs):
        # return settings.HURUMAP.get('theme')
        context = settings.HURUMAP.get('theme')
        context['title'] = 'can i get context'
        return context
