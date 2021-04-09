#! /bin/bash
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install - r requirements.txt
pip3 install pytest
pip3 install pytest-cov

python3 -m pytest Service1 --cov=Service1 --cov-report=term-missing
python3 -m pytest Service2 --cov=Service2 --cov-report=term-missing
python3 -m pytest Service3 --cov=Service3 --cov-report=term-missing
python3 -m pytest Service4 --cov=Service4 --cov-report=term-missing