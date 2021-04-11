from flask import Flask, Response, request
from os import getenv
import random
import string

app = Flask(__name__)

@app.route('/hostname')
def hostname():
    return str(getenv('HOSTNAME'))

@app.route('/randomletter', methods=['GET'])
def random_letter_generator():
    letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = 3
    total = ''
    for i in range (num):
        random_letter = random.choice(letter_list)
        total += random_letter

    return str(total)

if __name__=='__main__':
    app.run(host = '0.0.0.0', port = 5002, debug = True)