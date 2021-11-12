# !/bin/bash

cd api

python3 -m venv venv
. venv/bin/activate

python3 -m ensurepip --upgrade
python3 -m pip install -r requirements.txt

flask run
