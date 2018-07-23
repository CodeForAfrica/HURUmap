import os

HURUMAP_DASHBOARD_APPS = [
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',

    # Wagtail apps
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.wagtailstyleguide',

    'modelcluster',
    'taggit',

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
]

HURUMAP_DASHBOARD_MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

# -------------------------------------------------------------------------------------
# E-mail config
# -------------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('HURUMAP_EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_PORT = os.environ.get('HURUMAP_EMAIL_PORT', 2525)
EMAIL_HOST_USER = os.environ.get('HURUMAP_EMAIL_HOST_USER', 'apikey')
EMAIL_HOST_PASSWORD = os.environ.get('HURUMAP_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.environ.get('HURUMAP_EMAIL_USE_TLS', True)

# -------------------------------------------------------------------------------------
# Wagtail config
# -------------------------------------------------------------------------------------

WAGTAIL_SITE_NAME = 'HURUmap'  # TODO: Fix
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get('HURUMAP_EMAIL_FROM', 'no-reply@hurumap.org')
WAGTAILADMIN_NOTIFICATION_USE_HTML = True


WAGTAIL_ENABLE_UPDATE_CHECK = False  # Because Wazimap doesn't work with Python3 yet.

# -------------------------------------------------------------------------------------
# Authentication Configs
# -------------------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    }
]

LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD='email'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}



