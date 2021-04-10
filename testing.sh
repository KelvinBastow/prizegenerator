#! /bin/bash
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest
pip3 install pytest-cov

python3 -m pytest service1 --cov=service1
python3 -m pytest service2 --cov=service2
python3 -m pytest service3 --cov=service3
python3 -m pytest service4 --cov=service4