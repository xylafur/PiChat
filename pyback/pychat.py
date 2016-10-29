from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
