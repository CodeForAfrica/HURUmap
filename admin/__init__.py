CMS_ADMIN_APPS = (
    # Wagtail apps
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.sites',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',

    # Third-party apps
    'taggit',
    'modelcluster'
)

CMS_ADMIN_MIDDLEWARE = [
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware'
]