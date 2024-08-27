#!/bin/sh

BASE_DIR=$(dirname "$(readlink -f "$0")")

pip3 install -r "$BASE_DIR/requirements.txt"
python3 "$BASE_DIR/main.py"
