#!/bin/bash

echo "Python Virtual Environment Setup For Linux"

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment is ready"

