from flask import request, jsonify
from flask_socketio import emit, send, join_room, leave_room
from .. import socketio
from . import socket
import time

@socketio.on('message')
def handle_message(message):
    print('connect success!')
    send({'status': '200', 'message': 'success!'})

def ack():
    print('message was received!')

@socketio.on('response', namespace='/test')
def give_response(data):
    # print(request.sid)
    # print('connect success!')
    # value = data.get('param')
    # print(value)
    emit('response',{'code':'200','msg':data}, callback=allowLogin)
    # weixin = 'oCJfqvgk_O60fQ9GIWSp-rrVTiDA'
    # user = User.query.filter_by(weixin=weixin).first()
    # token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    time.sleep(15)
    emit('response',{'code':'200','msg':'start to process...'})
    # emit('response',{'status':'200','token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0MmNhNDQ5ZGQxYTg0ZTAyYTY5MzIwZmRkZWNlYmI1ZCIsImV4cCI6MTUxMzY1NTIwNX0.XWDbfySWUSae2EcRfMZKJNraTj_KnBo6pETtoTrZ1BA'},callback=ack)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socket.route('/allowLogin', methods=['POST'])
def allowLogin():
    # emit('response',{'code':'200','msg':'start to process...'})
    # join_room(room)
    # return room
    data = request.get_json()
    sid = data['sid']
    socketio.emit('response', {'data': 'A NEW FILE WAS POSTED'}, room=sid)
    return jsonify({'message': 'no permission to request!'})