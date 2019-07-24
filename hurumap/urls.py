from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from hurumap import settings
from .views import GeographyCompareAPIView

STANDARD_CACHE_TIME = settings.HURUMAP['cache_secs']

urlpatterns = [
                url(
                    regex   = '^api/compare/(?P<geo_id1>\w+-\w+)/vs/(?P<geo_id2>\w+-\w+)/$',
                    view    = cache_page(STANDARD_CACHE_TIME)(GeographyCompareAPIView.as_view()),
                    kwargs  = {},
                    name    = 'api_geography_compare',
                ),] + \
                static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                wazimap_urlpatterns
