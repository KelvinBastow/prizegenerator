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
from random import random

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomnumber")
def random_number_generator():
    count = 0
    num_string = ""
    while(count < 6):
        ran_num = random_rangeint(1,9)
        num_string = num_string + str(ran_num)
        count = count + 1
    print (random.randint(0, 9))

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)

# set an emply list

# statt a loop that goes up to 6

# in the loop, randomize between 0 and 9

# add that random value to your empty list

# return the list.