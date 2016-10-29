
@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
