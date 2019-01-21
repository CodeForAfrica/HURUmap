import json

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404
from django.utils.module_loading import import_string
from django.utils.safestring import SafeString
from wazimap.data.utils import dataset_context, get_page_releases
from wazimap.geo import geo_data
from wazimap.profiles import enhance_api_data
from wazimap.views import GeographyDetailView


def _get_values(obj):
    try:
        return obj['values']['this']

    except TypeError:
        pass


def _get_description_of_data_point(obj):
    # check if it has name value
    if obj.has_key('name'):
        return obj['name']
    elif obj.has_key('metadata'):
        return obj['metadata']

    # check if it has metadata and metadata has name

    # else get the key and replace _ with space and capitalize
    pass


def get_data(d):
    for k, v in d.iteritems():
        if isinstance(v, dict) and not v.has_key('values') and k != 'metadata':
            get_data(v)
        elif isinstance(v, dict) and v.has_key('values'):
            print "{0} : {1}\n".format(k, _get_values(v))
            yield k
        else:
            pass


class PDFView(GeographyDetailView):
    adjust_slugs = True
    default_geo_version = None
    template_name = 'pdf_data_template.html'

    def get_context_data(self, *args, **kwargs):
        page_context = {}

        # load the profile
        profile_method = settings.WAZIMAP.get('profile_builder', None)
        self.profile_name = settings.WAZIMAP.get('default_profile', 'default')

        if not profile_method:
            raise ValueError(
                "You must define WAZIMAP.profile_builder in settings.py")
        profile_method = import_string(profile_method)

        year = self.request.GET.get('release',
                                    geo_data.primary_release_year(self.geo))
        if settings.WAZIMAP['latest_release_year'] == year:
            year = 'latest'

        with dataset_context(year=year):
            profile_data = profile_method(self.geo, self.profile_name,
                                          self.request)

        profile_data['geography'] = self.geo.as_dict_deep()
        profile_data['primary_releases'] = get_page_releases(
            settings.WAZIMAP['primary_dataset_name'], self.geo, year)

        profile_data = enhance_api_data(profile_data)
        page_context.update(profile_data)

        return page_context

    def get_template_names(self):
        return ['pdf_data_template.html']

