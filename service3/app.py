# These will both generate a random “Object”, 
# this object can be whatever you like as we encourage creativity in this project.

# You can create the “Object” however you like, some methods will be more complex but 
# therefore show a greater technical understanding and flexibility, 
# examples of how you can generate your “Object” are:

# A text generator with 2 different implementations available:

# One that creates 3 char Strings of lowercase letters
# One that creates 2 char String of uppercase letters

from flask import Flask
from os import getenv
from random import random

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomletter")
def random_letter_generator():
    count = 0
    string = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while(count < 6):
        new_letter = random.choice(alphabet)
        string = string + new_letter
        count = count + 1
    return()
    

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)