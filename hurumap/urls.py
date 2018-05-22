from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from hurumap import settings
from hurumap.admin.urls import urlpatterns as cms_urlpatterns

urlpatterns = cms_urlpatterns + wazimap_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
