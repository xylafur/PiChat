#!/usr/bin/python3

print "starting server..."


from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app=Flask(__name__)
@app.route('/')
def login():
    return render_template("index.html")







#===========Main===========#
if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')
