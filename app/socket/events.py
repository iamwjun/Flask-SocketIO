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
    print('connect success!')
    value = data.get('param')
    print(value)
    emit('response',{'code':'200','msg':'start to process...'})

    time.sleep(15)
    emit('response',{'code':'200','msg':'processed'},callback=ack)