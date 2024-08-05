#!/bin/sh
makemigrations.sh
echo 'EXECUTANDO MIGRATE.SH'
python manage.py migrate --noinput
