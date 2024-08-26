#!/bin/sh

apt install python3-venv -y
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
