#!/usr/bin/env bash

add-apt-repository ppa:fkrull/deadsnakes
apt-get update

# Install Python & Dependencies
wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
apt-get install python3.5 python3.5-dev libffi-dev -q -y
python3.5 /tmp/get-pip.py
rm /tmp/get-pip.py
