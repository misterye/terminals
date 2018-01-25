import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '840821'
app.config['MYSQL_DB'] = 'log'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
app.config['SECRET_KEY'] = 'gq49gr9jgfkw4k950wjkgjwlhfw0'
socketio = SocketIO(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized. Please login.', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@app.route('/index')
@is_logged_in
def index():
    user = session['username']
    return render_template('index.html', user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            global name
            name = data['name']
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username
                flash("Welcome.", 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            cur.close()
        else:
            error = 'Not found.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash("Logged out.", 'success')
    return redirect(url_for('login'))

def messageReceived():
    print('Message Received!')

@socketio.on('my_event')
def handleMyevent(json):
    print("Handling my event: %s" % json)
    socketio.emit('my_response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', debug=True)
