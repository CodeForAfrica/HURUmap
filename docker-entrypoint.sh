#!/bin/bash

createdb hurumap                          # Create DB
python manage.py migrate --noinput        # Apply database migrations
cat hurumap/sql/*.sql | psql              # Upload tables / data
python manage.py compilescss              # Compile SCSS (offline)
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /src/logs/gunicorn.log
touch /src/logs/access.log
tail -n 0 -f /src/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --name hurumap \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class gevent \
    --log-level=info \
    --log-file=/src/logs/gunicorn.log \
    --access-logfile=/src/logs/access.log \
    --reload \
    hurumap.wsgi:application
