#!/bin/sh
echo Creating environment
virtualenv .env

echo Install PIP inside virtual environment
./.env/bin/easy_install pip

echo Installing dependencies
./.env/bin/pip install -E .env -r ./helpers/pip-requirements.txt
