from django.conf import settings
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from wazimap.geo import geo_data, LocationNotFound
from wazimap.views import GeographyDetailView
from weasyprint import HTML, CSS

from .utils import raw_data_for_geography


def pdf_view(request, **kwargs):
    version = request.GET.get('geo_version', None)
    geo_id = kwargs.get('geography_id', None)

    try:
        geo_level, geo_code = geo_id.split('-', 1)
        geo = geo_data.get_geography(geo_code, geo_level, version)
        page_context = {'geo': geo}
        raw_data = raw_data_for_geography(geo_code, geo_level)
        page_context['raw_data'] = raw_data
        page_context['geo'] = geo

        html_template = render_to_string(
            'pdf_data_template.html', context=page_context)
        pdf_file = HTML(string=html_template,
                        base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="hurumap-data.pdf"'
        return response
    except (ValueError, LocationNotFound):
        raise Http404


