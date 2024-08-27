#!/bin/bash

BASE_DIR=$(dirname "$(readlink -f "$0")")
cd "$BASE_DIR"

sudo apt install -y python3-venv
git pull

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
python3 main.py
