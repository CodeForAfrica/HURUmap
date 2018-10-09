# HURUmap Makefile
# ----------------

# HURUmap base

base:
	docker build --no-cache -t codeforafrica/hurumap-base:0.1.2 contrib/base
	docker build -t codeforafrica/hurumap-base:latest contrib/base
	docker push codeforafrica/hurumap-base:0.1.2
	docker push codeforafrica/hurumap-base:latest


# HURUmap app

build:
	docker-compose build

image-latest:
	docker build --no-cache -t codeforafrica/hurumap:latest .
	docker push codeforafrica/hurumap:latest

image-release:
	docker build --no-cache -t codeforafrica/hurumap:1.0.1
	docker push codeforafrica/hurumap:1.0.1


# Development

web:
	rm -fr static/*  # Workaround for whitenoise busyness in dev
	docker-compose up web

compilescss:
	docker-compose exec web ./manage.py compilescss
	rm -fr static/*
	docker-compose exec web ./manage.py collectstatic --noinput
