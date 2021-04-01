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
    backend_hostname = requests.get("http://backend:5001/hostname")
    random = requests.get("http://backend:5001/randomint")
    random = requests.get("http://backend:5001/randomstr")


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kelvinrules@mysql:3306/prizegenerator'

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email, ' Name: ', self.first_name, ' ', self.last_name, '\n'])

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)