FROM python:3.7-stretch as hurumap
ENV DEBIAN_FRONTEND noninteractive

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

# Install requirements
RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends apt-utils \
    && apt-get -qq install -y --no-install-recommends apt-utils postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip install -q -U pip setuptools gunicorn[gevent] shapely \
    git+https://github.com/CodeForAfricaLabs/wazimap.git#egg=wazimap \
    && pip install -q -e .[dashboard]

# Expose port server
EXPOSE 8000

COPY ./contrib/docker/entrypoint/hurumap.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [ "--name", "hurumap", "--reload", "hurumap.wsgi:application" ]


# HURUmap Kenya (for development purposes)
# ----------------------------------------
FROM hurumap as hurumap-kenya

WORKDIR $APP_SRVHOME
RUN mkdir hurumap_apps \
    && wget -qO- https://github.com/CodeForAfrica/HURUmap-apps/archive/feature/python3.tar.gz | tar -xz --strip=1 -C hurumap_apps

WORKDIR $APP_SRVHOME/hurumap_apps

ENV HURUMAP_APP="hurumap_ke"
ENV DJANGO_SETTINGS_MODULE="hurumap_ke.settings"
