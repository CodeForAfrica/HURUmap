from collections import OrderedDict
from wazimap.settings import *  # noqa

from hurumap.dashboard.settings import *  #noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('David Lemayian', 'david@codeforafrica.org'),
    ('Phillip Ahereza', 'ahereza@codeforafrica.org'),
    ('Support CfAfrica', 'support@codeforafrica.org')
)

MANAGERS = ADMINS

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + HURUMAP_DASHBOARD_MIDDLEWARE

TIME_ZONE = 'Africa/Nairobi'
LANGUAGE_CODE = 'en-ke'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'census.context_processors.api_url',
                'wazimap.context_processors.wazimap_settings',
                'hurumap.context_processors.hurumap_settings',
            ],
        },
    },
]

INSTALLED_APPS = ['hurumap', 'hurumap.dashboard'] + HURUMAP_DASHBOARD_APPS + INSTALLED_APPS

ROOT_URLCONF = 'hurumap.urls'


# -------------------------------------------------------------------------------------
# HURUmap Config
# -------------------------------------------------------------------------------------

HURUMAP = WAZIMAP

# -------------------------------------------------------------------------------------
# Website Details

HURUMAP['name'] = 'HURUmap'
HURUMAP['url'] = 'https://hurumap.org'

HURUMAP['description'] = 'gives infomediaries like journalists and Civic ' \
                         'activists an easy \'plug & play\' toolkit for ' \
                         'finding and embedding interactive data ' \
                         'visualizations into their storytelling'
HURUMAP['title_tagline'] = 'Making Census Data Easy to Use'

HURUMAP['facebook'] = 'CodeForAfrica'
HURUMAP['twitter'] = '@Code4Africa'
HURUMAP['email'] = 'hello@hurumap.org'
HURUMAP['blog_url'] = 'https://medium.com/code-for-africa'

HURUMAP['github_url'] = 'https://github.com/CodeForAfrica/HURUmap'
HURUMAP['openafrica_url'] = 'https://africaopendata.org'

# -------------------------------------------------------------------------------------
# Google Analytics

# Default tracker. Blank means no default tracking will be set (see
# `ga_tracking_ids` for multiple, named trackers support.
HURUMAP['ga_tracking_id'] = 'UA-44795600-8'

# Multiple trackers.
# Supports sending data to multiple properties from a single page. All these
# will be named trackers (t1, t2, ..., tn).
HURUMAP['ga_tracking_ids'] = []


# -------------------------------------------------------------------------------------
# Geography Details

HURUMAP['country_code'] = 'KE'
HURUMAP['country_name'] = 'Kenya'
HURUMAP['country_profile'] = 'country-KE-Kenya'

# Define the profile to load

hurumap_profile = os.environ.get('HURUMAP_PROFILE', 'census')
HURUMAP['default_profile'] = 'census'
HURUMAP['profile_builder'] = 'hurumap.profiles.{}.get_profile'.format(
    hurumap_profile)

HURUMAP['default_geo_version'] = os.environ.get('DEFAULT_GEO_VERSION', '2009')
HURUMAP['legacy_embed_geo_version'] = '2009'

HURUMAP['geodata'] = 'hurumap.geo.GeoData'
HURUMAP['geometry_data'] = {
    '2009': {
        'country': 'geo/country.topojson',
        'county': 'geo/county.topojson'
    }
}
HURUMAP['levels'] = {
    'country': {
        'plural': 'countries',
        'children': ['county'],
    },
    'county': {
        'plural': 'counties',
    }
}
HURUMAP['comparative_levels'] = ['country']

# Map config
HURUMAP['map_centre'] = [0.3051933453207569, 37.908818734483155]
HURUMAP['map_zoom'] = 6


# -------------------------------------------------------------------------------------
# Showcase Stories

HURUMAP['showcase_stories'] = [
    {
        'title':  'Marakwet locals intercept lorry ferrying 30 donkeys as demand for meat rises',
        'author': 'Stephen Rutto',
        'brief':  'Marakwet East locals intercepted a lorry transporting 30 donkeys in Chesoi, on suspicion that the animals had been stolen from from other areas.',
        'link':   'http://www.the-star.co.ke/news/2016/11/04/marakwet-locals-intercept-lorry-ferrying-30-donkeys-as-demand-for-meat_c1449795',
        'img':    STATIC_URL + 'img/showcase/donkeys.jpg'
    },
    {
        'title':  'Two suspected thugs shot dead in Nairobi as crime rate soars',
        'author': 'Nancy Agutu',
        'brief':  'Two suspected thugs were shot dead in two separate incidents on Tuesday evening, and three guns with more than 30 bullets recovered.',
        'link':   'http://www.the-star.co.ke/news/2016/10/19/two-suspected-thugs-shot-dead-in-nairobi-as-crime-rate-soars_c1440749',
        'img':    STATIC_URL + 'img/showcase/crime.jpg'
    },
    {
        'title':  'Narok, Homa Bay and West Pokot top in early pregnancy',
        'author': 'Monicah Mwangi',
        'brief':  'About one in every five teenage girls between 15-19 years have either had a live birth or are pregnant with their first child, according to a report by the United Nations Population Fund.',
        'link':   'http://www.the-star.co.ke/news/2016/11/02/narok-homa-bay-and-west-pokot-top-in-early-pregnancy_c1447958',
        'img':    STATIC_URL + 'img/showcase/early-pregnancy.jpg'
    }
]

# -------------------------------------------------------------------------------------
# Topics

HURUMAP['topics'] = OrderedDict()

HURUMAP['topics']['census'] = {
    'topic': 'census',
    'name': 'census 2009',
    'icon': '/static/img/census.png',
    'order': 1,
    'desc': 'Census data collected in 2009 provided by the Kenya National \
                Bureau of Statistics',
    'profiles': [
        'Demographics',
        'Households',
        'Protests',
        'School fires',
        'Crime report',
        'Employment',
        'Voter registration 2015',
        'Voter registration 2017',
        'Religion'
    ]
}

HURUMAP['topics']['education'] = {
    'topic': 'education',
    'name': 'education',
    'icon': '/static/img/education.png',
    'desc': 'Education data from Twaweza',
    'profiles': [
        'Education',
    ]
}

HURUMAP['topics']['health'] = {
    'topic': 'health',
    'name': 'health',
    'icon': '/static/img/health.png',
    'order': 2,
    'desc': 'Health data collected in 2014 by the Kenya National Bureau of \
                Statistics ',
    'profiles': [
        'Contraceptive use',
        'Maternal care indicators',
        'Knowledge of HIV prevention methods',
        'ITN',
        'Fertility',
        'Vaccinations',
        'Type treatment',
        'Nutrition',
        'Health ratios'
    ]
}

HURUMAP['topics']['development'] = {
    'topic': 'development',
    'name': 'development',
    'icon': '/static/img/development.png',
    'order': 3,
    'desc': 'Crop production and Livestock population for the year 2014 \
            provided by the Ministry of Agriculture, Livestock and Fisheries.',
    'profiles': [
        'Crop production',
        'Livestock'
    ],
}


WAZIMAP = HURUMAP


# -------------------------------------------------------------------------------------
# Database Configs
# -------------------------------------------------------------------------------------

DATABASE_URL = os.environ.get('DATABASE_URL',
                              'postgresql://hurumap:hurumap@localhost/hurumap')

DATABASES['default'] = dj_database_url.parse(DATABASE_URL)
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['TEST'] = {
    'NAME': 'hurumap_test',
}


# -------------------------------------------------------------------------------------
# Wagtail + CMS Configs
# -------------------------------------------------------------------------------------
WAGTAIL_SITE_NAME = HURUMAP['name']
SITE_ID = 1

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

HURUMAP['primary_release_year'] = {
    'county': 2017,
}
HURUMAP['latest_release_year'] = '2017'
HURUMAP['primary_dataset_name'] = 'Voter Registration'
HURUMAP['available_release_years'] = {
    # Release years with data for geo_levels.
    # Only specify geo_levels with limited releases.
    # Other geo_levels have data for all releases.
    'county': [2015, 2017]
}
#

# -------------------------------------------------------------------------------------
# Logging Configs
# -------------------------------------------------------------------------------------

LOGGING['loggers']['hurumap'] = {'level': 'DEBUG' if DEBUG else 'INFO'}
