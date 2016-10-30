
from flask import Flask, render_template, request, redirect, url_for, Response, session, flash
from flask_login import LoginManager
from flask_socketio import SocketIO, send, emit
from functools import wraps

import location, usermanager, avaliablerooms
#from pyback.user import User
#import pyback.util

app=Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret!'
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)

#=========== session login stuff===========#
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


#=========== socketio stuff ===========#
#import pyback.pychat

@socketio.on('message') #Generic message event to server, for log purposes.
def handle_message(message):
    print('Received message: ' + message)
    send(message)
    return

#Not yet used
@socketio.on('userconnect')
def handle_connected(username):
    log = '%s connected. ' % (username)
    print(log)
    send(log)

@socketio.on('chat message')
def chat_message(username, message):
    log = '[%s] : %s' % (username, message)
    print(log)
    send(log)



#=========== app route stuff ==========#

@app.route('/', methods=['GET','POST'])
def login():
    if (request.method == 'GET'):
        return render_template("index.html")

    if (request.method == 'POST'):
        userName = request.form['userName']
        session['logged_in'] = True
        flash('You just logged in!')
        return redirect(url_for('avaliableRooms'))
    return render_template("index.html", error = None)


@app.route('/rooms')
@login_required
def avaliableRooms():
    temp = location.getLocation()
    flash('You just logged out.')
    return render_template("rooms.html")


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

#===========Main===========#
if __name__ == '__main__':
    #app.run(debug= True, host='0.0.0.0')
    socketio.run(app)
    print("Finished Initializing app and socket.")
