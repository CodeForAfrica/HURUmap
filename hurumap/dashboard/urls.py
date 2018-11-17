from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from hurumap.dashboard import settings

from hurumap.urls import urlpatterns as hurumap_urlpatterns
from hurumap.dashboard.views import UserProfileView

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              hurumap_urlpatterns + [
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^accounts/profile/$',
                      UserProfileView.as_view(), name='user_profile'),
                
                  url(r'^django-admin/', include(admin.site.urls)),

                  url(r'^dashboard/', include(wagtailadmin_urls)),
                  url(r'^documents/', include(wagtaildocs_urls)),
                  url(r'^', include(wagtail_urls)),
              ]
