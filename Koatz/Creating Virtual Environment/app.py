from unicodedata import name
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about")
def about():
    return "I am learning flask with Altschool"


@app.route("/ayodeji/<name>/<dob>/<dob2>")
def ayodeji(name, dob, dob2):
    return f"My name is {name} and I was born on {dob} {dob2}"


if __name__ == "__main__":
    app.run(debug=True)
