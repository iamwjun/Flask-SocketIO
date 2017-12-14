from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL, patch_request_class
from flask_cors import CORS, cross_origin
import pymysql
import os

socketio = SocketIO()
db = SQLAlchemy()
photos = UploadSet('PHOTO')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    configure_uploads(app, photos)
    patch_request_class(app)
    patch_request_class(app, 32 * 1024 * 1024)
    CORS(app)

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