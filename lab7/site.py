
from flask import Flask
app = Flask(__name__)
host = '0.0.0.0'


@app.route("/")
def hello():
    return "<h1 style='color:blue'>lab7 here!</h1>"


if __name__ == "__main__":
    app.run(debug=True, host=host, port=80)
