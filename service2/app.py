# These will both generate a random “Object”, 
# this object can be whatever you like as we encourage creativity in this project.

# You can create the “Object” however you like, some methods will be more complex but 
# therefore show a greater technical understanding and flexibility, 
# examples of how you can generate your “Object” are:

# A number generator with 2 different implementations available:

# One that creates a 6-digit number.
# One that creates an 8-digit number.

from flask import Flask
from os import getenv
from random import randint, randstr

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomstr")
def random_generator():
    return str(randstr("A" "a", "Z" "z"))

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)