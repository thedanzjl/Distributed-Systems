
from flask import Flask, render_template, send_file
app = Flask(__name__)
host = '0.0.0.0'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/page2")
def page2():
    return render_template('page2.html')

#
# @app.route('/cloudflare.jpg')
# def image1():
#     return send_file('cloudflare.jpg', mimetype='image/jpg')
#
#
# @app.route('/nginx_conf.jpg')
# def image2():
#     return send_file('nginx_conf.jpg', mimetype='image/jpg')


if __name__ == "__main__":
    app.run(debug=True, host=host, port=5000)
