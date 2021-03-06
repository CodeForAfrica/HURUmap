from django.conf.urls import include, url
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from hurumap.dashboard import settings

from hurumap.urls import urlpatterns as hurumap_urlpatterns
from hurumap.dashboard.views import UserProfileView

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              [
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^accounts/profile/$',
                      UserProfileView.as_view(), name='user_profile'),

                  url(r'^dashboard/', include(wagtailadmin_urls)),
                  url(r'^documents/', include(wagtaildocs_urls)),
                  url(r'^', include(wagtail_urls)),
              ] + \
              hurumap_urlpatterns
