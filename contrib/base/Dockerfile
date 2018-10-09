FROM python:2.7-stretch
ENV DEBIAN_FRONTEND noninteractive

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install gdal-bin python-gdal libgdal-dev -y
RUN apt-get install postgresql-client -y

# Upgrade pip + setuptools
RUN pip install -q -U pip setuptools gunicorn

# GDAL Installs
# TODO: Remove after mapit installation
RUN pip install -q GDAL==2.1.3 --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN pip install -q "Shapely>=1.5.13"
