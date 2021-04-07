# The core service – this will render the Jinja2 templates you need to interact with your application, 
# it will also be responsible for communicating with the other 3 services, 
# and finally for persisting some data in an SQL database.

from flask import Flask, render_template, Response, request
# from flask_sqlalchemy import SQLAlchemy
import requests
# from os import getenv

app = Flask(__name__)
# db = SQLAlchemy(app)
@app.route("/", methods=['GET'])
@app.route("/prizegenerator", methods=['GET'])
def home():
    service_four_default_response=requests.get("http://service4:5003/").json()
    return f'{service_four_default_response["prize_money"]}'

# {service_four_default_response["random_letter"]} {service_four_default_response["random_number"]}
  
    return render_template('homepage.html', form=form, message=error)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kelvinrules@34.105.153.83/prizegenerator'

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)