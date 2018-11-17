from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from hurumap import settings

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              wazimap_urlpatterns
