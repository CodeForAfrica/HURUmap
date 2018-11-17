COMPOSE = docker-compose
DEVDOCKER = $(COMPOSE) exec web

build:
	$(COMPOSE) build

web:
	rm -fr static/*  # Workaround for whitenoise busyness in dev
	$(COMPOSE) up web

compilescss:
	$(DEVDOCKER) ./manage.py compilescss
	rm -fr static/*
	$(DEVDOCKER) ./manage.py collectstatic --noinput
