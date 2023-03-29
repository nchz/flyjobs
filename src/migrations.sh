#!/bin/bash -e

python manage.py makemigrations
python manage.py migrate
