"""
this code will Copy the previous task to a new script that starts a Flask web application with additional python web page
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    this calls the first 'hello_hbnb' web page
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    this calls the second 'hbnb' web page
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    # Replace '_' with spaces
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python/<text>", strict_slashes=False)
def python(text):
    # Replace '_' with spaces
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)