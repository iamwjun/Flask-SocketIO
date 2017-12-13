import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'thisisasecret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/news?charset=utf8'
    JSON_SORT_KEYS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True