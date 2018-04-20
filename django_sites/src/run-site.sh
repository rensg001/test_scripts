#!/usr/bin/env bash
source env.sh
# wait for db service
resolve_service db:5433
wait_tcp_dependency ${RESOLVE_IP} ${RESOLVE_PORT}

# do database migration
python manage.py makemigrations
python manage.py migrate
uwsgi --ini uwsgi.ini