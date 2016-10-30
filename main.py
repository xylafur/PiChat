
from flask import Flask, render_template, request, redirect, url_for, Response, session
from flask_login import LoginManager
from flask_socketio import SocketIO, emit
import location
from functools import wraps


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

@app.route('/')

#=========== app route stuff ==========#
@app.route('/', methods=['GET','POST'])
def login():
    if (request.method == 'GET'):
        return render_template("index.html")

    if (request.method == 'POST'):
        userName = request.form['userName']
        session['logged_in'] = True
        return redirect(url_for('avaliableRooms'))
    return render_template("index.html", error = None)

@app.route('/', methods=['POST'])
def afterLogin():
    userName = request.form['userName']
    return redirect(url_for('avaliableRooms'))


@app.route('/rooms')
@login_required
def avaliableRooms():
    temp = location.getLocation()
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
