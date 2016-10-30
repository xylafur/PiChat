
from flask import Flask, render_template, request, redirect, url_for, Response, session
from flask_login import LoginManager
from flask_socketio import SocketIO, emit
from functools import wraps

import location, roommanager, usermanager
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

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



#=========== socketio stuff ===========#
#import pyback.pychat

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    #handle message shit here


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

        #so now when we redirect to the url we are passing in the JSON
        #string as a variable called newUser
        return redirect(url_for('avaliableRooms', newUser = userJson))
    return render_template("index.html", error = None)


@app.route('/rooms')
@login_required
def avaliableRooms():
    #gets the JSON variabe new user that is passed
    newUser = request.args['newUser']
    return render_template("rooms.html")

@app.route('/create')
@login_required
def newRoom():

    return redirect(url_for('avaliableRooms', newUser = userJson))


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
