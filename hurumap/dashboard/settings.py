import os

from hurumap.settings import *  #noqa

INSTALLED_APPS = INSTALLED_APPS + [
        'django.contrib.auth',
        'django.contrib.sessions',
        # Wagtail apps
        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail.core',
        'wagtail.contrib.styleguide',
        'wagtail.contrib.settings',

        'modelcluster',
        'taggit',

        # allauth apps
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',

        'hurumap.dashboard',
        'storages',
    ]

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'django.contrib.messages.middleware.MessageMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'hurumap.dashboard.urls'

SITE_ID = 1


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

WAGTAIL_SITE_NAME = HURUMAP['name']
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get('HURUMAP_EMAIL_FROM', 'no-reply@hurumap.org')
WAGTAILADMIN_NOTIFICATION_USE_HTML = True

WAGTAIL_ENABLE_UPDATE_CHECK = False  # Because Wazimap doesn't work with Python3 yet.

TEMPLATES[0]['OPTIONS']['context_processors'] = TEMPLATES[0]['OPTIONS'][
                                                 'context_processors'] + [
                                                 'wagtail.contrib.settings.context_processors.settings']


# -------------------------------------------------------------------------------------
# Media and Static Files Settings
# -------------------------------------------------------------------------------------

MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT', os.path.join(BASE_DIR, "media"))
MEDIA_URL = '/media/'

USE_S3 = strtobool(str(os.getenv('USE_S3', False)))

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = '{}.s3.{}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'hurumap.dashboard.storage_backends.StaticStorage'
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
    DEFAULT_FILE_STORAGE = 'hurumap.dashboard.storage_backends.PublicMediaStorage'


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

