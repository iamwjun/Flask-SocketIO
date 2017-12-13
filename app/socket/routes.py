from flask import render_template
from . import socket

@socket.route('/', methods=['GET'])
def index():
    return render_template("index.html")