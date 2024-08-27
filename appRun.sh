#!/bin/sh

BASE_DIR=$(dirname "$(readlink -f "$0")")

echo "RUNNING: cd "$BASE_DIR""
cd "$BASE_DIR"

echo "RUNNING: git pull"
git pull

echo "RUNNING: python3 -m venv .venv"
python3 -m venv .venv

echo "RUNNING: source .venv/bin/activate"
source .venv/bin/activate

echo "RUNNING: pip3 install -r requirements.txt"
pip3 install -r requirements.txt

echo "RUNNING: python3 main.py"
python3 main.py
