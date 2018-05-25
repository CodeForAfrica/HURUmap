from django.conf.urls import include, url
from django.conf.urls.static import static
from wazimap.urls import urlpatterns as wazimap_urlpatterns
from django.contrib import admin

from hurumap import settings
from hurumap.admin.urls import urlpatterns as hurumap_admin_urlpatterns
from hurumap.views import UserProfileView


urlpatterns = [
                url(r'^django_admin/', include(admin.site.urls)), ] \
              + hurumap_admin_urlpatterns + wazimap_urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
