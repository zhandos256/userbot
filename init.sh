#!/bin/bash

# create virtualenv
/usr/bin/python3 -m venv .env
. ./.env/bin/activate

pip install -U pip && pip install -r requirements.txt

# Create folders
mkdir src/migrations/versions
mkdir src/locales

# Go to src
cd src

# Init DB
python init_db.py

# Create initial migrations
alembic revision -m "initial"
alembic upgrade head