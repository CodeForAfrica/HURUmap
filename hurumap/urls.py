from django.conf.urls import include, url
from wazimap.urls import urlpatterns as wazimap_urlpatterns

from admin.urls import blogs_urls, wagtailadmin_urls, wagtaildocs_urls

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^blog/', include(blogs_urls)),
] + wazimap_urlpatterns
