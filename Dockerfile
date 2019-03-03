FROM python:3.7-stretch as hurumap-base
ENV DEBIAN_FRONTEND noninteractive

# Upgrade OS Dependencies + Install Postgresql Client
RUN apt-get -qq update && apt-get -qq install postgresql-client -y --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install and upgrade pip + setuptools + gunicorn with gevent
RUN pip install -q -U pip setuptools gunicorn[gevent] shapely


FROM hurumap-base as hurumap

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

# Workaround for latest wazimap (releases branch)
# Comment out when wazimpa package becomes regularly updated with latest features
RUN pip install -q git+https://github.com/CodeForAfricaLabs/wazimap.git@feature/python3#egg=wazimap

# Install hurumap + wazimap
RUN pip install -q -e .

# Expose port server
EXPOSE 8000

COPY ./contrib/docker/entrypoint/hurumap.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [ "--name", "hurumap", "--reload", "hurumap.wsgi:application" ]


# HURUmap Dashboard
# -----------------
FROM hurumap as hurumap-dashboard

ENV DJANGO_SETTINGS_MODULE="hurumap.dashboard.settings"

RUN pip install -q -e .[dashboard]
CMD [ "--name", "hurumap_dashboard", "--reload", "hurumap.wsgi:application" ]


# HURUmap Kenya (for development purposes)
# ----------------------------------------
FROM hurumap as hurumap-kenya

WORKDIR $APP_SRVHOME
RUN git clone --single-branch --branch feature/python3 https://github.com/CodeForAfrica/HURUmap-apps.git hurumap_apps

WORKDIR $APP_SRVHOME/hurumap_apps

ENV DJANGO_SETTINGS_MODULE="hurumap_ke.settings"
