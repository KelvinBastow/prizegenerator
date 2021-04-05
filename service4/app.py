# This service will also create an “Object” however this “Object” must be based upon the results of service 
# #2 + #3 using some pre-defined rules. Please see below for an example of how this logic can look.

# The complexity of your logic here is up to you, again a simple implementation is allowed, 
# however, may not showcase your full understanding of the technology.

# A prize generator with 2 different implementations available, 
#in both cases the prize is determined by the char string and number generated above.

# One for when the service is feeling generous (bigger rewards)
# One for when the service is not feeling generous (smaller rewards)


# These will both generate a random “Object”, 
# this object can be whatever you like as we encourage creativity in this project.

# You can create the “Object” however you like, some methods will be more complex but 
# therefore show a greater technical understanding and flexibility, 
# examples of how you can generate your “Object” are:

# A text generator with 2 different implementations available:

# One that creates 3 char Strings of lowercase letters
# One that creates 2 char String of uppercase letters

from flask import Flask, render_template, Response, request
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")
def home():
    hostname = getenv("HOSTNAME")
    return hostname

@app.route("/service-two")
def service_two():
    service2_hostname = requests.get("http://service2:5001/hostname")
    service2_response = requests.get("http://service2:5001/randomnumber").text
    return f'{service2_response}'



@app.route("/service-three")
def service_three():
    service3_hostname = requests.get("http://service3:5002/hostname")
    service3_response = requests.get("http://service3:5002/randomletter").text
    return f'{service3_response}'


if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)