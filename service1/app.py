from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class PrizeGenerator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_number = db.Column(db.String(50), nullable = False)
    random_letter = db.Column(db.String(50), nullable = False)

@app.route('/', methods=['GET'])
@app.route('/prizegenerator', methods=['GET'])
def home():
    service_four_default_response=requests.get('http://service4:5003/prizecreator').json()
    prize = f'{service_four_default_response["prize_money"]}'
    randomprize = PrizeGenerator(random_number = service_four_default_response["random_number"], random_letter = service_four_default_response["random_letter"])
    db.session.add(randomprize)
    db.session.commit()

    return render_template('homepage.html', message=prize)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)