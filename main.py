from flask import Flask, render_template, request, redirect, url_for
import location

app=Flask(__name__)

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def afterLogin():
    userName = request.form['userName']
    return redirect(url_for('avaliableRooms'))

@app.route('/rooms')
def avaliableRooms():
    temp = location.getLocation()
    return str(temp)

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')
