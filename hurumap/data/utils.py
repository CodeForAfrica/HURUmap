"""
Data utilities HURUmap adds to help with data preparations for visualization.
"""

# A dist that can be used to return from `get_profile` so that the rendering
# template can decide whether to hide or show CtA in case of missing data.
# e.g. to hide the viz in case of missing data, one would put the following
# code in the template
#
# {% if not data.is_missing %}
#   ... viz code goes here ..
# {% endif %}
LOCATION_NOT_FOUND_DIST = {
    'is_missing': True,
    'name': 'No Data Found',
    'numerators': {
        'this': 0
    },
    'values': {
        'this': 0
    },
}


def create_single_value_dist(name='', value=0):
    """
    Create a dist from a given single `value` named `name`.
    """

    return {
        'name': name,
        'numerators': {
            'this': value
        },
        'values': {
            'this': value
        },
        'metadata': {}
    }
