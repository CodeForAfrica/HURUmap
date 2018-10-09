FROM codeforafrica/hurumap-base:0.1.2
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

# Upgrade pip + setuptools, install hurumap
RUN pip install -q -U pip setuptools gunicorn
RUN pip install -q .


# Server
EXPOSE 8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
