# These will both generate a random “Object”, 
# this object can be whatever you like as we encourage creativity in this project.

# You can create the “Object” however you like, some methods will be more complex but 
# therefore show a greater technical understanding and flexibility, 
# examples of how you can generate your “Object” are:

# A text generator with 2 different implementations available:

# One that creates 3 char Strings of lowercase letters
# One that creates 2 char String of uppercase letters

from flask import Flask, Response, request
from os import getenv
import random
import string

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomletter", methods=['GET'])
def random_letter_generator():
    letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num =6
    total = ""
    for i in range (num):
        random_letter = random.choice(letter_list)
        total += random_letter

    return total

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)