FROM python:2.7-stretch
ENV DEBIAN_FRONTEND noninteractive

MAINTAINER Code for Africa

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install binutils libproj-dev gdal-bin python-gdal libgdal-dev -y
RUN apt-get install libtiff5-dev libjpeg62-turbo-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev \
    tcl8.6-dev tk8.6-dev python-tk -y
RUN apt-get install postgresql-client -y
