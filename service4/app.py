from flask import Flask, jsonify
import requests
from os import getenv

app = Flask(__name__)

@app.route('/prizecreator')
def prizecreator():
    hostname = getenv('HOSTNAME')
    random_number = requests.get('http://service2:5001/randomnumber').text
    random_letter = requests.get('http://service3:5002/randomletter').text
    # prize generator here, create code to mutlipy number 1-9 by how many repetitions there are of a singular letter
    if random_letter.count(random_letter[0]) > 1:
        prize_money = int(random_number) * 10
    else:
        prize_money = int(random_number) * 5
    packet = { 
        "random_number": random_number, "random_letter": random_letter, "prize_money": prize_money
    }
    return jsonify(packet)


if __name__=='__main__':
    app.run(host = '0.0.0.0', port = 5003, debug = True)