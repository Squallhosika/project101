#!/bin/bash

#apt-get update
#apt-get install netcat

set -e

#MYSQL_HOST=db
#MYSQL_PORT=3306
#WAIT=0

#while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
#    sleep 3
#    WAIT=$(($WAIT + 1))
#      if [ "$WAIT" -gt 15 ]; then
#        echo "Error: Timeout wating for Mysql to start"
#        exit 1
#      fi
#done

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Make migrations
python manage.py makemigrations client

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000