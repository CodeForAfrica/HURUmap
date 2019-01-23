from wazimap.views import GeographyDetailView

from .utils import raw_data_for_geography



class PDFView(GeographyDetailView):
    adjust_slugs = True
    default_geo_version = None
    template_name = 'pdf_data_template.html'

    def get_context_data(self, *args, **kwargs):
        page_context = {}

        raw_data = raw_data_for_geography(self.geo.geo_code, self.geo.geo_level)
        page_context['raw_data'] = raw_data
        page_context['geo'] = self.geo
        return page_context

    def get_template_names(self):
        return ['pdf_data_template.html']

