from flask import Flask, request, jsonify, make_response, current_app, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL, patch_request_class
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import uuid
import jwt
import os
import urllib.parse
from app import db, photos
from . import api
from ..model.models import User, News

# CORS(app)

# visit proxy
# app = current_app._get_current_object()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return  jsonify({'status': '401', 'message': 'Token is missing!'})

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'status': '401', 'message': 'Token is invalid!'})

        return f(current_user, *args, **kwargs)
    
    return decorated
        

@api.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user or not current_user.admin:
        return jsonify({'message': 'no permission to request!'})

    try:
        users = User.query.all()

        output = []

        for user in users:
            user_data = {}
            user_data['public_id'] = user.public_id
            user_data['name'] = user.name
            user_data['password'] = user.password
            user_data['admin'] = user.admin
            user_data['create_time'] = user.create_time
            user_data['update_time'] = user.update_time
            output.append(user_data)

        return jsonify({'users': output})
    except:
        return jsonify({'status': '401', 'message': 'An exception occurred during registration'})

@api.route('/user/<public_id>', methods=['GET'])
@token_required
def get_users_byid(current_user, public_id):
    if not current_user or not current_user.admin:
        return jsonify({'message': 'No permission to request!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'status': '404', 'message': 'user does not exist'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    user_data['create_time'] = user.create_time
    user_data['update_time'] = user.update_time

    return jsonify({'user': user_data})

@api.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user or not current_user.admin:
        return jsonify({'message': 'no permission to request!'})

    try:
        data = request.get_json()

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(public_id=str(uuid.uuid4().hex), name=data["name"], weixin=data["weixin"], password=hashed_password, admin=False, create_time=datetime.now(), update_time=datetime.now())
        db.session.add(new_user)
        db.session.commit()
    
    except:
        return jsonify({'status': '401', 'message': 'An exception occurred during registration'})

    return jsonify({'status': '200', 'meessage': 'new user created!'})

@api.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user or not current_user.admin:
        return jsonify({'message': 'No permission to request!'})
    
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'status': '404', 'message': 'User does not exist'})
    user.admin = True
    db.session.commit()

    return jsonify({'status': '200', 'message': 'The user has been promoted!'})

@api.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user or not current_user.admin:
        return jsonify({'message': 'No permission to request!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'status': '404', 'message': 'user does not exist'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'status': '200', 'message': 'The user has been deleted!'})

# use password and name login
# @api.route('/login')
# def login():
#     auth = request.authorization
#     if not auth or not auth.username or not auth.password:
#         return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
#     user = User.query.filter_by(name=auth.username).first()
#     if not user:
#         return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
#     if check_password_hash(user.password, auth.password):
#         token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
#         return jsonify({'token': token.decode('UTF-8')})
#     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

@api.route('/getToken', methods=['POST'])
def getToken():
    try:
        data = request.get_json()
        weixin = data['weixin']
        user = User.query.filter_by(weixin=weixin).first()
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token.decode('UTF-8')})
    except:
        return jsonify({'status': '401', 'message': 'an exception occurs!'})

@api.route('/isUserExists/<weixin>', methods=['GET'])
def isUserExists(weixin):
    try:
        user = User.query.filter_by(weixin=weixin).first()
        if user:
            return jsonify({'status': '200', 'message': 'ok!'})
        return jsonify({'status': '404', 'message': 'The user does not exist!'})
    
    except:
        return jsonify({'status': '401', 'message': 'An exception occurred during registration'})

@api.route('/filter', methods=['POST'])
@token_required
def filter_news(current_user):
    try:
        data = request.get_json()

        news = News.query.order_by(News.id.desc()).limit(data['page_size']).offset((data['page_num'] - 1) * data['page_size'])
        count = News.query.count()
        output = []

        for item in news:
            items = {}
            items['id'] = item.id
            items['title'] = item.title
            items['public_id'] = item.public_id
            items['create_time'] = item.create_time.strftime('%Y-%m-%d %H:%M:%S')
            items['update_time'] = item.update_time.strftime('%Y-%m-%d %H:%M:%S')
            items['update_by'] = item.update_by
            items['views'] = item.views
            items['is_hot'] = item.is_hot
            items['is_del'] = item.is_del
            items['news_type'] = item.news_type
            items['news_keys'] = item.news_keys
            items['thumb'] = item.thumb
            output.append(items)

        return jsonify({'news': output, 'count': count})

    except:
        return jsonify({'status': '401', 'message': 'an exception occurs!'})

@api.route('/news', methods=['GET'])
@token_required
def get_all_news(current_user):
    try:
        news = News.query.order_by(News.id.desc()).all()
        output = []

        for item in news:
            items = {}
            items['id'] = item.id
            items['title'] = item.title
            items['public_id'] = item.public_id
            items['create_time'] = item.create_time.strftime('%Y-%m-%d %H:%M:%S')
            items['update_time'] = item.update_time.strftime('%Y-%m-%d %H:%M:%S')
            items['update_by'] = item.update_by
            items['views'] = item.views
            items['is_hot'] = item.is_hot
            items['is_del'] = item.is_del
            items['news_type'] = item.news_type
            items['news_keys'] = item.news_keys
            items['thumb'] = item.thumb
            output.append(items)

        return jsonify({'news': output})

    except:
        return jsonify({'status': '401', 'message': 'an exception occurs!'})

@api.route('/news', methods=['POST'])
@token_required
def create_news(current_user):
    if not current_user:
        return jsonify({'message': 'No permission to request!'})

    try:
        data = request.get_json()

        new_news = News(
            public_id=str(uuid.uuid4().hex),
            create_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            update_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            release_time=data['release_time'],
            update_by=current_user.public_id,
            views=int(0),
            title=data['title'],
            body=data['body'],
            summary=data['summary'],
            is_hot=data['is_hot'],
            is_del=data['is_del'],
            news_type=data['news_type'],
            news_keys=data['news_keys'],
            thumb=data['thumb']
        )
        db.session.add(new_news)
        db.session.commit()
        
        return jsonify({'status': '200', 'meessage': 'new news created!'})

    except:
        return jsonify({'status': '401', 'meessage': 'an exception occurs!'})

@api.route('/news/<public_id>', methods=['GET'])
@token_required
def get_news_byid(current_user, public_id):    
    if not current_user:
        return jsonify({'message': 'No permission to request!'})

    item = News.query.filter_by(public_id=public_id).first()

    if not item:
        return jsonify({'status': '404', 'message': 'news does not exist'})

    item.views=item.views+1
    db.session.commit()

    items = {}
    items['id'] = item.id
    items['title'] = item.title
    items['public_id'] = item.public_id
    items['create_time'] = item.create_time.strftime('%Y-%m-%d %H:%M:%S')
    items['update_time'] = item.update_time.strftime('%Y-%m-%d %H:%M:%S')
    items['release_time'] = item.release_time.strftime('%Y-%m-%d %H:%M:%S')
    items['update_by'] = item.update_by
    items['views'] = item.views
    items['body'] = item.body
    items['summary'] = item.summary
    items['is_hot'] = item.is_hot
    items['is_del'] = item.is_del
    items['news_type'] = item.news_type
    items['news_keys'] = item.news_keys
    items['thumb'] = item.thumb

    return jsonify({'news': items})

@api.route('/news/<public_id>', methods=['PUT'])
@token_required
def promote_news(current_user, public_id):
    data = request.get_json()

    item = News.query.filter_by(public_id=public_id).first()

    if not item:
        return jsonify({'status': '404', 'message': 'news does not exist'})

    try:
        item.title=data['title']
        item.update_time=datetime.utcnow()
        item.update_by=current_user.public_id
        item.release_time=data['release_time']
        item.body=data['body']
        item.summary=data['summary']
        item.is_hot=data['is_hot']
        item.is_del= data['is_del']
        item.news_type= data['news_type']
        item.news_keys= data['news_keys']
        item.thumb= data['thumb']
        db.session.commit()

        return jsonify({'status': '200', 'message': 'The news has been promoted!'})
    except:
        return jsonify({'status': '401', 'meessage': 'an exception occurs!'})

@api.route('/news/<public_id>', methods=['DELETE'])
@token_required
def delete_news(current_user, public_id):
    news = News.query.filter_by(public_id=public_id).first()

    if not news:
        return jsonify({'message': 'news does not exist'}), 404

    if not news.is_del:
        news.is_del = True
        db.session.commit()
    else:
        db.session.delete(news)
        db.session.commit()

    return jsonify({'status': '200', 'message': 'delete successful'})

@api.route('/uploadimage', methods=['POST'])
@token_required
def upload(current_user):
    if request.method == 'POST' and 'photo' in request.files:
        try:
            filename = photos.save(request.files['photo'], name=''+ datetime.utcnow().strftime("%Y%m") +'/'+ str(uuid.uuid4().hex) +'.')
            return jsonify({'status': '200', 'path': filename})
        except Exception as inst:
            return jsonify({'status': '403', 'message': 'Abnormal when storing pictures'})
    return jsonify({'status': '404', 'message': 'The picture is missing'})