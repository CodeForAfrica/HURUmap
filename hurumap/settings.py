from collections import OrderedDict
from wazimap.settings import *  # noqa
from distutils.util import strtobool

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('David Lemayian', 'david@codeforafrica.org'),
    ('Phillip Ahereza', 'ahereza@codeforafrica.org'),
    ('Support CfAfrica', 'support@codeforafrica.org')
)

MANAGERS = ADMINS

TIME_ZONE = 'Africa/Nairobi'
LANGUAGE_CODE = 'en-ke'

TEMPLATES[0]['OPTIONS']['context_processors'] = TEMPLATES[0]['OPTIONS'][
                                                    'context_processors'] + [
                                                    'hurumap.context_processors.hurumap_settings']

INSTALLED_APPS = ['hurumap'] + INSTALLED_APPS

ROOT_URLCONF = 'hurumap.urls'

# -------------------------------------------------------------------------------------
# HURUmap Config
# -------------------------------------------------------------------------------------

HURUMAP = WAZIMAP

# -------------------------------------------------------------------------------------
# Website Details

HURUMAP['name'] = os.environ.get('HURUMAP_NAME', 'HURUmap')
HURUMAP['url'] = os.environ.get('HURUMAP_URL', 'https://hurumap.org/')

HURUMAP['description'] = 'gives infomediaries like journalists and Civic ' \
                         'activists an easy \'plug & play\' toolkit for ' \
                         'finding and embedding interactive data ' \
                         'visualizations into their storytelling'
HURUMAP['title_tagline'] = 'Making Census Data Easy to Use'

HURUMAP['facebook'] = os.environ.get('HURUMAP_FACEBOOK', 'CodeForAfrica')
HURUMAP['twitter'] = os.environ.get('HURUMAP_TWITTER', '@Code4Africa')
HURUMAP['email'] = os.environ.get('HURUMAP_EMAIL', 'hello@hurumap.org')
HURUMAP['blog_url'] = os.environ.get('HURUMAP_BLOG_URL',
                                     'https://medium.com/code-for-africa')

HURUMAP['github_url'] = os.environ.get('HURUMAP_GITHUB_URL',
                                       'https://github.com/CodeForAfrica/HURUmap')
HURUMAP['openafrica_url'] = os.environ.get('HURUMAP_OPENAFRICA_URL',
                                           'https://openafrica.net/')

# -------------------------------------------------------------------------------------
# Google Analytics

# Default tracker. Blank means no default tracking will be set (see
# `ga_tracking_ids` for multiple, named trackers support.
HURUMAP['ga_tracking_id'] = os.environ.get('HURUMAP_GA_TRACKING_ID',
                                           'UA-44795600-8')

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

HURUMAP['default_geo_version'] = os.environ.get('HURUMAP_DEFAULT_GEO_VERSION',
                                                '2009')
HURUMAP['legacy_embed_geo_version'] = '2009'

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

HURUMAP['geodata'] = 'hurumap.geo.GeoData'
HURUMAP['mapit'] = {}
HURUMAP['geometry_data'] = {
    '2009': {
        'country': 'geo/country.topojson',
        'county': 'geo/county.topojson'

    }
}

# leaflet JS tile layer (https://leafletjs.com/reference.html#tilelayer)
HURUMAP['tile_layer'] = {
    'url_template': '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'options': {
        'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
        'subdomains': 'abc',
        'maxZoom': 17
    }
}

# Mapit (http://mapit.poplus.org)
use_mapit = os.environ.get('USE_MAPIT', False)
HURUMAP['USE_MAPIT'] = strtobool(str(use_mapit))

if HURUMAP['USE_MAPIT']:
    # use mapit settings
    HURUMAP['geodata'] = 'hurumap.mapit_geo.GeoData'
    HURUMAP['geometry_data'] = {}
    HURUMAP['mapit'] = {
        'url': 'https://mapit.hurumap.org',
        'country_code': 'KE',
        'generations': {
            '2009': '1',
            None: '1',
            # this should be based on the default_geo_version wazimap setting
        },
        'code_type': 'KEN',
        'level_simplify': {
            'country': 0,
            'county': 0
        },
        'map_country': {
            'centre': [0.3051933453207569, 37.908818734483155],
            'zoom': 6
        }
    }

# -------------------------------------------------------------------------------------
# Showcase Stories

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

# -------------------------------------------------------------------------------------
# Releases

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

# WAZIMAP TUTORIAL VIDEOS
HURUMAP['video_links'] = OrderedDict([
    ('intro',
     'https://www.youtube.com/embed/lXKDBoRSqxo?list=PL7MJ_sFHs952CYcKHPQp786HVVy83nBwH'),
    ('table_view',
     'https://www.youtube.com/embed/KQ8jM51S1Ik?list=PL7MJ_sFHs952CYcKHPQp786HVVy83nBwH'),
    ('map_view',
     'https://www.youtube.com/embed/SFsTnYkTKx0?list=PL7MJ_sFHs952CYcKHPQp786HVVy83nBwH'),
    ('distribution_view',
     'https://www.youtube.com/embed/WCftaPfULSg?list=PL7MJ_sFHs952CYcKHPQp786HVVy83nBwH'),
    ("comparing_places",
     'https://www.youtube.com/embed/7mSZnXFHFxo?list=PL7MJ_sFHs952CYcKHPQp786HVVy83nBwH')
])

# color scheme

HURUMAP['theme'] = {
    'charts': {
        # http://colorbrewer2.org/
        'colorbrewer': {
            'Set2': [
                "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3",
                "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"
            ],
            # saturated version of Colorbrewer 'Set2' scheme, so the unhovered
            # state, at 80% opacity, looks like the original colorbrewer color
            'Set2S': [
                "#33b5b5", "#ed8b69", "#6295cc", "#dd85c0",
                "#8ecc23", "#fccd06", "#dbba97", "#aaaaaa"
            ],
        },
        'color_scale': 'Set2S',
        'chart_height': 160
    }
}

# -------------------------------------------------------------------------------------
# Logging Configs
# -------------------------------------------------------------------------------------

LOGGING['loggers']['hurumap'] = {'level': 'DEBUG' if DEBUG else 'INFO'}
