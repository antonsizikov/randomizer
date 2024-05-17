#!/bin/bash

export FLET_FORCE_WEB_SERVER=true
export FLET_SERVER_PORT=9112

BASEDIR=$(dirname "$0")

source ../.venv/bin/activate
python3.12 ${BASEDIR}/main.py
