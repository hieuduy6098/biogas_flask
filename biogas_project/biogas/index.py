from flask import session, request, render_template, url_for, redirect, jsonify
from __init__ import app
from model import *
from  processDataChart import getDataByIdDaily, getDataByIdMonthly, getDataByIdHourly, getEnergyByIdDaily
from datetime import datetime, timedelta
from sqlalchemy.inspection import inspect

app.secret_key='asdsdfsdfs13sdf_df%&'
app.permanent_session_lifetime = timedelta(days=1)

# login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userNamePost = request.form['user']
        passWordPost = request.form['pswd']
        if user.query.filter_by(userName=userNamePost).all():
            if user.query.filter_by(passWord=passWordPost).all():
                if userNamePost == 'admin':
                    session.permanent = True
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
            nowDay = datetime.now().day
            userData = user.query.filter_by(idMachine=idMachine).first()
            timeDataChartPower, valueDataChartPower = getDataByIdHourly(idMachine, 'elepwt', nowDay)
            timeDataChartEnergy, valueDataChartEnergy = getEnergyByIdDaily(idMachine, 'eleewh', nowMonth)

            return render_template('person.html', user=userData,
                                   timeDataChartPower=timeDataChartPower,valueDataChartPower=valueDataChartPower,
                                   timeDataChartEnergy=timeDataChartEnergy, valueDataChartEnergy=valueDataChartEnergy)
    except:
        return redirect(url_for('login'))


@app.route('/chartPerson', methods=['POST', 'GET'])
def chartPerson():
    try:
        if request.method == "POST":
            data = request.get_json()
            if data['typeMessage']=='dailyEnergy':
                timeDataChartEnergy, valueDataChartEnergy = getEnergyByIdDaily(data['idMachine'], data['typeChart'], data['month'])
                jsonData = {
                    'time': timeDataChartEnergy,
                    'value': valueDataChartEnergy,
                }
                return jsonify(jsonData)
            elif data['typeMessage']=='monthlyEnergy':
                timeDataChartEnergy, valueDataChartEnergy = getDataByIdMonthly(data['idMachine'], data['typeChart'], data['year'])
                jsonData = {
                    'time': timeDataChartEnergy,
                    'value': valueDataChartEnergy,
                }
                return jsonify(jsonData)
            elif data['typeMessage']=='reloadDailyPower':
                timeDataChartEnergy, valueDataChartEnergy = getDataByIdDaily(data['idMachine'], data['typeChart'], data['month'])
                jsonData = {
                    'time': timeDataChartEnergy,
                    'value': valueDataChartEnergy,
                }
                return jsonify(jsonData)
            elif data['typeMessage']=='reloadHourlyPower':
                timeDataChartEnergy, valueDataChartEnergy = getDataByIdHourly(data['idMachine'], data['typeChart'], data['day'])
                jsonData = {
                    'time': timeDataChartEnergy,
                    'value': valueDataChartEnergy,
                }
                return jsonify(jsonData)
    except:
        print("error process request")


@app.route('/chart', methods=['POST', 'GET'])
def chart():
    try:
        if request.method == "POST":
            data = request.get_json()
            if data['sensor'][0:3] == 'ele':
                result = electrical.query.filter(electrical.idMachine_id == data['idMachine']).filter(electrical.time > data['start']).filter(electrical.time < data['end']).all()
            elif data['sensor'][0:3] == 'env':
                result = environment.query.filter(environment.idMachine_id == data['idMachine']).filter(environment.time > data['start']).filter(environment.time < data['end']).all()
            elif data['sensor'][0:3] == 'ope':
                result = operation.query.filter(operation.idMachine_id == data['idMachine']).filter(operation.time > data['start']).filter(operation.time < data['end']).all()
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
            listSensor={'eles':'t???c ?????','eleva':'??i???n ??p pha a','elevb':'??i???n ??p pha b','elevc':'??i???n ??p pha c','elevna':'??i???n ??p d??y ab','elevab':'??i???n ??p d??y bc','elevbc':'??i???n ??p d??y ca',
                        'elevca':'??i???n ??p pha tb','elevla':'??i???n ??p d??y tb','eleia':'d??ng pha a','eleib':'d??ng pha b','eleic':'d??ng pha c', 'eleiav':'d??ng pha tb','elepwa':'c??ng su???t pha a',
                        'elepwb':'c??ng su???t pha b','elepwc':'c??ng su???t pha c','elepwt':'c??ng su???t pha tb', 'elepfa':'h??? s??? c??ng su???t pha a','elepfb':'h??? s??? c??ng su???t pha a',
                        'elepfc':'h??? s??? c??ng su???t pha c','elepft':'h??? s??? c??ng su???t pha tb','elef':'t???n s???','eleewh':'??i???n n??ng', 'eleevah':'n??ng l?????ng', 'eletop':'tg v???n h??nh',
                        'elethdva':'THD_Van/Vab','elethdvb':'THD_Vbn/Vbc','elethdvc':'THD_Vcn/Vca','elethdia':'THD_Ia','elethdib':'THD_Ib','elethdic':'THD_Ic',
                        'envtw':'nhi???t ????? n?????c','envpo':'??p su???t d???u', 'envo2':'n???ng ????? O2', 'envh2s':'n???ng ????? H2S',
                        'opepidsp':'T???c ????? ?????t','opepidout':'T???c ????? ?????u ra pid','opevpb':'G??c m??? van biogas', 'opepb':'??p su???t tank biogas', 'opevsfb':'T???c ????? ph???n h???i'}
            return render_template('adminPerson.html', user = userData, listSensor= listSensor)
    except:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5000,debug=False)
