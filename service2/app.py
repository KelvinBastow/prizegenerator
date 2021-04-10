from flask import Flask
from flask import Response, request
from os import getenv
import random

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomnumber", methods=['GET'])
def random_number_generator():
    return f"{random.randint(1,20)}"


if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)