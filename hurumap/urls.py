from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from hurumap import settings
from hurumap.views import PDFView, pdf_view

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              wazimap_urlpatterns
urlpatterns += [
    url(
        regex='^data/pdf/(?P<geography_id>\w+-\w+)(-(?P<slug>[\w-]+))?/$',
        view=pdf_view,
        name='data-pdf',)
]
