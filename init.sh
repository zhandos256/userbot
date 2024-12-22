#!/bin/bash

/usr/bin/python3 -m venv .env
. ./.env/bin/activate

pip install -U pip && pip install -r requirements.txt

mkdir src/migrations/versions
mkdir src/locales

cd src

alembic revision -m "initial"
alembic upgrade head
