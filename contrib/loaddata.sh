#!/bin/bash

cat hurumap/sql/*.sql | psql  # Load tables / data into DB (TBD)
# python manage.py loaddata fixtures/hurumap_fixtures.json
