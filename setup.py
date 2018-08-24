from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()

install_requires = [
    'django==1.9.13',
    'wagtail==1.13.1',
    'wazimap',
    'libsass==0.13.3',
    # https://github.com/CodeForAfrica/HURUmap-apps/issues/66
    'whitenoise==3.3.1',
    # https://github.com/CodeForAfrica/HURUmap-apps/issues/66
    'django-allauth==0.34.0'
]

dependency_links = [
    'https://github.com/OpenUpSA/wazimap/tarball/2cdc95447c95f20d1ba9bb2e272eef25075e14ff#egg=wazimap']

setup(
    name='hurumap',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='HURUmap helps storytellers and campaigners use data to add context and depth to stories.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/CodeForAfricaLabs/HURUmap',

    # Author details
    author='Code for Africa',
    author_email='hello@codeforafrica.org',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    include_package_data=True,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    dependency_links=dependency_links,

    setup_requires=[
        "setuptools_git >= 1.0",
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['nose', 'flake8'],
        'test': ['nose', 'flake8'],
        'gdal': ['GDAL', 'Shapely>=1.5.13'],
    },
)
