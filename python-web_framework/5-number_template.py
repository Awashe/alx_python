"""
this script starts a Flask web application which renders template 
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

@app.route('/python/', defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    # Replace '_' with spaces
    text = text.replace("_", " ")
    return "Python {}".format(text)

"""
@app.route("/number/<n>", strict_slashes=False)
def display_number(n):
    # Check that n is an integer
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return abort(404)
"""
@app.route('/number/<int:n>')
def display_number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('templates/5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)