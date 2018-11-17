FROM python:2.7-stretch
ENV DEBIAN_FRONTEND noninteractive

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install gdal-bin python-gdal libgdal-dev -y
RUN apt-get install postgresql-client -y

# Upgrade pip + setuptools
RUN pip install -q -U pip setuptools

# Install gunicorn with gevent
RUN pip install -q -U gunicorn[gevent]

# GDAL Installs
# TODO: Remove after mapit installation
RUN pip install -q GDAL==2.1.3 --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN pip install -q "Shapely>=1.5.13"

# Add version
ADD VERSION .


# Set env variables used in this Dockerfile
# Local directory with project source

ENV APP_SRC=.
# Directory in container for all project files
ENV APP_SRVHOME=/src
# Directory in container for project source files
ENV APP_SRVPROJ=/src/hurumap

# Create application subdirectories
WORKDIR $APP_SRVHOME
RUN mkdir media static logs
VOLUME ["$APP_SRVHOME/media/", "$APP_SRVHOME/logs/"]

# Add application source code to SRCDIR
ADD $APP_SRC $APP_SRVPROJ
WORKDIR $APP_SRVPROJ

# Install hurumap
RUN pip install -q .


# Server
EXPOSE 8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
