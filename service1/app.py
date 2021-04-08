from os import error
from flask import Flask, render_template, Response, request
# from flask_sqlalchemy import SQLAlchemy
import requests
# from os import getenv

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = getenv(DATABASE_URI)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS] = False
# db = SQLAlchemy(app)

@app.route("/", methods=['GET'])
@app.route("/prizegenerator", methods=['GET'])
def home():
    service_four_default_response=requests.get("http://service4:5003/").json()
    prize = f'{service_four_default_response["prize_money"]}'

    return render_template('homepage.html', message=prize)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)