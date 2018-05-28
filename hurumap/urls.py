from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from hurumap import settings
from hurumap.dashboard.urls import urlpatterns as hurumap_dashboard_urlpatterns
from hurumap.views import UserProfileView


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              wazimap_urlpatterns + hurumap_dashboard_urlpatterns
