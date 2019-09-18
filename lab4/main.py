
from flask import Flask, render_template
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    
    # return render_template("welcome.html")
    return "\
<html>\
\
<head>\
	\
	<link rel='shortcut icon' href='static/favicon.ico'>\
\
</head>\
\
<header> <title> My favourite meme </title> </header>\
\
<body> \
\
How many people have seen my meme: {}<br>\
<img src='static/meme.jpg' />\
</body>\
\
</html>\
    ".format(visits)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)


