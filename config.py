from flask_uploads import IMAGES
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'thisisasecret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/news?charset=utf8'
    JSON_SORT_KEYS = False
    UPLOADED_PHOTO_DEST = os.path.dirname(os.path.abspath(__file__)) + '/app/static/image'
    UPLOADED_PHOTO_ALLOW = IMAGES

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True