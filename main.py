from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')
