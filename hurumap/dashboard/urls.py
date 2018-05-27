from django.conf.urls import include, url
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from hurumap.views import UserProfileView

urlpatterns = [
    url(r'^dashboard/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^', include(wagtail_urls)),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$',
        UserProfileView.as_view(), name='user_profile'),
]
