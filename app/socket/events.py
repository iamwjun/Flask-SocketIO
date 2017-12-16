from flask_socketio import emit, send
from .. import socketio
import time

@socketio.on('message')
def handle_message(message):
    print('connect success!')
    send({'status': '200', 'message': 'success!'})

def ack():
    print('message was received!')

@socketio.on('response',namespace='/test')
def give_response(data):
    # print('connect success!')
    # value = data.get('param')
    # print(value)
    # emit('response',{'code':'200','msg':'start to process...'})
    # weixin = 'oCJfqvgk_O60fQ9GIWSp-rrVTiDA'
    # user = User.query.filter_by(weixin=weixin).first()
    # token = jwt.encode({'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(days=1)}, current_app.config['SECRET_KEY'], algorithm='HS256')
    time.sleep(15)
    emit('response',{'status':'200','token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0MmNhNDQ5ZGQxYTg0ZTAyYTY5MzIwZmRkZWNlYmI1ZCIsImV4cCI6MTUxMzQ5OTg2MX0.XU3mdGUJG9GCRHzZ2ycsmz6rWtFKQgeTIKFK1cWIolY'},callback=ack)