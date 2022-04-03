from flask import Flask, session, request, render_template, url_for, redirect
from biogas import app
from model import *

app.secret_key='asdsdfsdfs13sdf_df%&'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userNamePost = request.form['user']
        passWordPost = request.form['pswd']
        if users.query.filter_by(userName=userNamePost).all():
            if users.query.filter_by(passWord=passWordPost).all():
                user = users.query.filter_by(passWord=passWordPost).all()
                session['userName'] = request.form['user']
                session['idMachine'] = user[0].idMachine
                return redirect(url_for('index', idMachine = user[0].idMachine))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/index/<idMachine>')
def index(idMachine):
    try:
        if idMachine in session['idMachine']:
            return render_template('index.html')
    except:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
