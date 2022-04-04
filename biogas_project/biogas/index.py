from flask import session, request, render_template, url_for, redirect, jsonify
from biogas import app
from model import user as userDb

app.secret_key='asdsdfsdfs13sdf_df%&'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userNamePost = request.form['user']
        passWordPost = request.form['pswd']
        if userDb.query.filter_by(userName=userNamePost).all():
            if userDb.query.filter_by(passWord=passWordPost).all():
                user = userDb.query.filter_by(passWord=passWordPost).all()

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
            user = userDb.query.filter_by(idMachine=idMachine).first()
            return render_template('index.html', user = user)
    except:
        return redirect(url_for('login'))


@app.route('/test', methods=['POST', 'GET'])
def test():
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            return jsonify({"id":1})
    except:
        print("error process request")


if __name__ == '__main__':
    app.run(debug=True)
