# The core service – this will render the Jinja2 templates you need to interact with your application, 
# it will also be responsible for communicating with the other 3 services, 
# and finally for persisting some data in an SQL database.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)
@app.route("/")
def home():
    hostname = getenv("HOSTNAME")
    backend_hostname = requests.get("http://service1:5000/hostname")
    random = requests.get("http://service4:5001/randomstr")
    

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kelvinrules@mysql:3306/prizegenerator'

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)