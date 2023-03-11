# import modules from class
from flask import Flask, render_template

# using app, an object of the class Flask
app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Vancouver',
    'salary': '60000'
  },
    {
    'id': 2,
    'title': 'Data Analyst2',
    'location': 'Vancouver',
    'salary': '70000'
  },
    {
    'id': 3,
    'title': 'Data Analyst3',
    'location': 'Vancouver',
    'salary': '80000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
