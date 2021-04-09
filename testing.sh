#! /bin/bash
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install - r requirements.txt
pip3 install pytest
pip3 install pytest-cov

python3 -m pytest --cov=, --cov-report=missing-term