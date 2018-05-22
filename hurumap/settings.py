from wazimap.settings import *  # noqa
from admin import CMS_ADMIN_APPS, CMS_ADMIN_MIDDLEWARE

ADMINS = (('David Lemayian', 'david@codeforafrica.org'),)
MANAGERS = ADMINS

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + CMS_ADMIN_MIDDLEWARE

TIME_ZONE = 'Africa/Nairobi'
LANGUAGE_CODE = 'en-ke'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'census.context_processors.api_url',
    'wazimap.context_processors.wazimap_settings',
    'hurumap.context_processors.hurumap_settings',
)


HURUMAP = WAZIMAP

INSTALLED_APPS =CMS_ADMIN_APPS + ['hurumap', 'admin'] + INSTALLED_APPS

ROOT_URLCONF = 'hurumap.urls'


HURUMAP['name'] = 'HURUmap'
HURUMAP['url'] = 'https://hurumap.org'

WAZIMAP['geodata'] = 'hurumap.geo.GeoData'
HURUMAP['geometry_data'] = {}

# Default tracker. Blank means no default tracking will be set (see
# `ga_tracking_ids` for multiple, named trackers support.
HURUMAP['ga_tracking_id'] = 'UA-44795600-8'

# Multiple trackers.
# Supports sending data to multiple properties from a single page. All these
# will be named trackers (t1, t2, ..., tn).
HURUMAP['ga_tracking_ids'] = []

HURUMAP['facebook'] = 'CodeForAfrica'
HURUMAP['twitter'] = '@Code4Africa'
HURUMAP['contact_email'] = 'hello@hurumap.org'

HURUMAP['github_url'] = 'https://github.com/CodeForAfrica/HURUmap'
HURUMAP['openafrica_url'] = 'https://open.africa/'
HURUMAP['description'] = 'gives infomediaries like journalists and Civic ' \
                         'activists an easy \'plug & play\' toolkit for ' \
                         'finding and embedding interactive data ' \
                         'visualizations into their storytelling'
HURUMAP['title_tagline'] = 'Making Census Data Easy to Use'

HURUMAP['showcase_stories'] = [
    {
        'title': 'Marakwet locals intercept lorry ferrying 30 donkeys as demand for meat rises',
        'author': 'Stephen Rutto',
        'brief': 'Marakwet East locals intercepted a lorry transporting 30 donkeys in Chesoi, on suspicion that the animals had been stolen from from other areas.',
        'link': 'http://www.the-star.co.ke/news/2016/11/04/marakwet-locals-intercept-lorry-ferrying-30-donkeys-as-demand-for-meat_c1449795',
        'img': STATIC_URL + 'img/showcase/donkeys.jpg'
    },
    {
        'title': 'Two suspected thugs shot dead in Nairobi as crime rate soars',
        'author': 'Nancy Agutu',
        'brief': 'Two suspected thugs were shot dead in two separate incidents on Tuesday evening, and three guns with more than 30 bullets recovered.',
        'link': 'http://www.the-star.co.ke/news/2016/10/19/two-suspected-thugs-shot-dead-in-nairobi-as-crime-rate-soars_c1440749',
        'img': STATIC_URL + 'img/showcase/crime.jpg'
    },
    {
        'title': 'Narok, Homa Bay and West Pokot top in early pregnancy',
        'author': 'Monicah Mwangi',
        'brief': 'About one in every five teenage girls between 15-19 years have either had a live birth or are pregnant with their first child, according to a report by the United Nations Population Fund.',
        'link': 'http://www.the-star.co.ke/news/2016/11/02/narok-homa-bay-and-west-pokot-top-in-early-pregnancy_c1447958',
        'img': STATIC_URL + 'img/showcase/early-pregnancy.jpg'
    }
]

WAZIMAP = HURUMAP

LOGGING['loggers']['hurumap'] = {'level': 'DEBUG' if DEBUG else 'INFO'}

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://hurumap:hurumap@localhost/hurumap')

DATABASES['default'] = dj_database_url.parse(DATABASE_URL)
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['TEST'] = {
    'NAME': 'test_hurumap',
}
