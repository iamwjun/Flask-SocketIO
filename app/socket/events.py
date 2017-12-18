from flask import request, jsonify, current_app
from flask_socketio import emit, send, join_room, leave_room
from datetime import datetime, timedelta
import time
import jwt
from .. import socketio
from . import socket
from ..model.models import User

@socket.route('/allowLogin', methods=['POST'])
def allowLogin():
    try:
        data = request.get_json()
        weixin = data['weixin']
        sid = data['sid']
        user = User.query.filter_by(weixin=weixin).first()
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
        print(token)
        # json = jsonify({'status': '200', 'token': token.decode('UTF-8')})
        json = {'status': '200', 'token': token.decode('UTF-8')}
        socketio.send(json, room=sid, namespace='/allow')
        return jsonify({'status': '200', 'message': 'ok!'})
    except:
        return jsonify({'status': '401', 'message': 'an exception occurs!'})

@socketio.on('response', namespace='/test')
def give_response(data):
    emit('response',{'code':'200','msg':data}, callback=allowLogin)
    
    time.sleep(15)
    emit('response',{'code':'200','msg':'start to process...'})

@socketio.on('join', namespace='/allow')
def on_join(data):
    print(request.sid)
    room = data['room']
    print(request.sid, room)
    join_room(room)
    send(request.sid + ' has entered the room.', room=room)

@socketio.on('leave', namespace='/allow')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)