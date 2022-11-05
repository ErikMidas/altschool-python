from unicodedata import name
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about")
def about():
    return "I am learning flask with Altschool"


@app.route("/ayodeji/<name>/<string:month>/<int:day>")
def ayodeji(name, month, day):
    return f"My name is {name} and I was born on {month} {day}"


@app.route('/post/<int:id>')
def post_id(id):
    return f"This post has a user id of {id}"


if __name__ == "__main__":
    app.run(debug=True)
