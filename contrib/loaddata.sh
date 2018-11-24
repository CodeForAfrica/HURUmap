#!/bin/bash

cat hurumap/sql/*.sql | psql # Upload tables / data (TBD)
# python manage.py loaddata fixtures/hurumap_fixtures.json
