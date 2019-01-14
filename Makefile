COMPOSE = docker-compose

build:
	$(COMPOSE) build

web:
	$(COMPOSE) up web

compilescss:
	$(COMPOSE) exec web python manage.py compilescss
	$(COMPOSE) exec web python manage.py collectstatic --clear --noinput

enter:
	$(COMPOSE) exec web bash

migrate:
	$(COMPOSE) exec web python manage.py migrate

loaddata:
	# Load the DB with data
	$(COMPOSE) exec -T web ./contrib/loaddata.sh

createsuperuser:
	$(COMPOSE) exec web python manage.py createsuperuser


clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

release:
	./contrib/docker/release.sh

release-build:
	./contrib/docker/release-build.sh
