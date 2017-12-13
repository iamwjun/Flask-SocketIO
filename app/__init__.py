from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

socketio = SocketIO()
db = SQLAlchemy()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object('config.DevelopmentConfig')

    from .socket import socket as socket_blueprint
    from .api import api as api_blueprint
    from .model import model as model_blueprint
    app.register_blueprint(socket_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(model_blueprint)

    socketio.init_app(app)
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app