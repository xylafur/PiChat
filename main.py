
from flask import Flask, render_template, request, redirect, url_for, Response, session, flash
from flask_login import LoginManager
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from functools import wraps

import location, roommanager, usermanager
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> FrontEnd
=======

>>>>>>> c310da3d692f24aea3f8b3405d2baa3f14007ed3
#from pyback.user import User
#import pyback.util

app=Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret!'
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)


def log(alog):
    print(astr)
    return alog

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

@socketio.on('connect')
def on_connect(data):
    send('connected.')

@socketio.on('disconnect')
def on_disconnect(data):
    global disconnected
    disconnected = '/'


@socketio.on('message')
def on_message(message):
    send(message)
    '''
    if message == 'test session':
        session['a'] = 'b'
    if message not in "test noackargs":
        return message
    '''

def on_join_room(data):
    join_room(data['room']) #data at room in the json

def on_leave_room(data):
    leave_room(data['room']) #data at room in the json


#=========== app route stuff ==========#

@app.route('/', methods=['GET','POST'])
def login():
    if (request.method == 'GET'):
        return render_template("index.html")

    if (request.method == 'POST'):
        userName = request.form['userName']
        userLocation = location.getLocation()
        userJson = usermanager.getUser(userName, userLocation)

        session['logged_in'] = True
<<<<<<< HEAD
<<<<<<< HEAD
        flash('You just logged in!')
=======
>>>>>>> FrontEnd
=======
        flash('You just logged in!')
>>>>>>> c310da3d692f24aea3f8b3405d2baa3f14007ed3

        #so now when we redirect to the url we are passing in the JSON
        #string as a variable called newUser
        return redirect(url_for('avaliableRooms', newUser = userJson))
    return render_template("index.html", error = None)


@app.route('/rooms')
@login_required
def avaliableRooms():
    #gets the JSON variabe new user that is passed
    newUser = request.args['newUser']
    return render_template("rooms.html", newUser = newUser)

@app.route('/create')
@login_required
def newRoom():
    return redirect(url_for('avaliableRooms', newUser = userJson))

@app.context_processor
def utility_processor():
    def createRoom(userJson):
        print(userJson)
        return("userJson")
    return dict(createRoom=createRoom)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You just logged out.')
    return redirect(url_for('login'))

#===========Main===========#
if __name__ == '__main__':
    #app.run(debug= True, host='0.0.0.0')
    socketio.run(app)
    print("Finished Initializing app and socket.")
