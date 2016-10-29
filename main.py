#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

app=Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret!'
socketio = SocketIO(app)


#=========== socketio stuff ===========#
#import pyback.pychat

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    #handle message shit here

'''
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)
'''


#=========== app route stuff ==========#

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def afterLogin():
    userName = request.form['userName']
    print(url_for('avaliableRooms'))
    return redirect(url_for('avaliableRooms'))

@app.route('/rooms')
def avaliableRooms():
    return render_template("rooms.html")


#===========Main===========#
if __name__ == '__main__':
    #app.run(debug= True, host='0.0.0.0')
    socketio.run(app)
    print("Finished Initializing app and socket.")
