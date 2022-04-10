from flask import session, request, render_template, url_for, redirect, jsonify
from biogas import app
from model import *
from  processDataChart import getDataByIdDaily
from datetime import datetime
from sqlalchemy.inspection import inspect

app.secret_key='asdsdfsdfs13sdf_df%&'


# login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userNamePost = request.form['user']
        passWordPost = request.form['pswd']
        if user.query.filter_by(userName=userNamePost).all():
            if user.query.filter_by(passWord=passWordPost).all():
                if userNamePost == 'admin':
                    userData = user.query.filter_by(passWord=passWordPost).all()
                    session['userName'] = request.form['user']
                    session['idMachine'] = userData[0].idMachine
                    return redirect(url_for('admin'))
                else:
                    userData = user.query.filter_by(passWord=passWordPost).all()
                    session['userName'] = request.form['user']
                    session['idMachine'] = userData[0].idMachine
                    return redirect(url_for('person', idMachine = userData[0].idMachine))
    return render_template('login.html')


#log out
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# index
@app.route('/person/<idMachine>')
def person(idMachine):
    try:
        if idMachine in session['idMachine']:
            nowMonth = datetime.now().month
            userData = user.query.filter_by(idMachine=idMachine).first()
            timeDataChart, valueDataChart = getDataByIdDaily(idMachine, 'elepwt', nowMonth)
            #print(nowMonth)
            return render_template('person.html', user=userData, timeDataChart=timeDataChart,valueDataChart=valueDataChart)
    except:
        return redirect(url_for('login'))


@app.route('/chart', methods=['POST', 'GET'])
def chart():
    try:
        if request.method == "POST":
            data = request.get_json()
            result = electrical.query.filter(electrical.idMachine_id == data['idMachine']).filter(electrical.time > data['start']).filter(electrical.time < data['end']).all()
            jsonData = {}
            for object in result:
                dictObject = object.__dict__
                jsonData.update({dictObject['time']: dictObject[data['sensor']]})
            return jsonify(jsonData)
    except:
        print("error process request")

@app.route('/admin')
def admin():
    try:
        if session['userName'] == 'admin':
            userData = user.query.filter_by(userName=session['userName']).first()
            userList = user.query.filter(user.userName.startswith('user')).all()
            return render_template('admin.html', user = userData, userList = userList)
    except:
        return redirect(url_for('login'))

# index
@app.route('/admin/<idMachine>')
def adminPerson(idMachine):
    try:
        if session['userName'] == 'admin':
            userData = user.query.filter_by(idMachine=idMachine).first()
            listSensor=['eles','eleva','elevb','elevc','elevna','elevab','elevbc','elevca','elevla','eleia','eleib','eleic','eleiav','elepwa','elepwb','elepwc','elepwt','elepfa','elepfb','elepfc','elepft','elef','eleewh','leevah','eletop','ethdva','ethdvb','ethdvc','ethdia','ethdib','ethdic',
                        'envtw','envpo','envo2','envh2s',
                        'opete','opetb','opepidsp','opepidout','opevpb','opepb','opevsfb']
            return render_template('adminPerson.html', user = userData, listSensor= listSensor)
    except:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)
