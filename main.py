#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit



app=Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret!'
socketio = SocketIO(app)

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
