# import module from class
from flask import Flask

# using app, an object of the class Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p> Hello! </p>"