from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def valid_login(username: str, password: str):
    return username == "test" and password == "test"

@app.route("/")
def index():
    # if 'login' in session and 'password' in session:
        return render_template('index.html')
    # return render_template('login.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if valid_login(request.form['login'], request.form['password']):
            session['login'] = request.form['login']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            return render_template('error.html', error='Incorrect Credentials!')

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))