from model import *
import pandas as pd
from datetime import datetime

def getDataByIdHourly(idMachine, idSensor, day):
    electricalDataList = electrical.query.filter_by(idMachine_id=idMachine).all()
    listTime = []
    listValue = []
    data = {
        'timestamp': listTime,
        'value': listValue,
    }
    for electricalData in electricalDataList:
        listTime.append(electricalData.__dict__['time'])
        listValue.append(electricalData.__dict__[idSensor])
    table = pd.DataFrame(data)
    # loc  dataframe
    table.sort_values(by='timestamp', inplace=True)
    table.drop_duplicates(subset='timestamp', inplace=True)
    table['timestamp'] //= 1000
    table['datetime'] = pd.to_datetime(table['timestamp'], unit='s')
    table['day'] = table['datetime'].dt.day
    table['hour'] = table['datetime'].dt.hour
    table = table[table['day'] == day]
    table1 = table.groupby(['hour'], as_index=False).mean()
    table1['value'] = round(table1['value'], 0)
    listDays = [*range(1, 25)]
    for i in table1.index:
        if table1.loc[i, 'hour'] in listDays:
            listDays.remove(table1.loc[i, 'hour'])
            # for j in listHours:
            #    list1 = [[j,0]]
    newList = []
    for j in listDays:
        newList.append([j, 0])
    df = pd.DataFrame(newList, columns=['hour', 'value'])
    table1 = pd.concat([table1, df], ignore_index=True)
    table1.sort_values(by='hour', inplace=True)
    # print(table1)
    listTime = []
    for i in table1['hour'].tolist():
        listTime.append(int(float(str(i))))
    listValue = table1['value'].tolist()
    return listTime, listValue

def getDataByIdDaily(idMachine, idSensor, month):
    electricalDataList = electrical.query.filter_by(idMachine_id=idMachine).all()
    listTime = []
    listValue = []
    data = {
        'timestamp': listTime,
        'value': listValue,
    }
    for electricalData in electricalDataList:
        listTime.append(electricalData.__dict__['time'])
        listValue.append(electricalData.__dict__[idSensor])
    table = pd.DataFrame(data)
    # loc  dataframe
    table.sort_values(by='timestamp', inplace=True)
    table.drop_duplicates(subset='timestamp', inplace=True)
    table['timestamp'] //= 1000
    table['datetime'] = pd.to_datetime(table['timestamp'], unit='s')
    table['date'] = table['datetime'].dt.date
    table['month'] = table['datetime'].dt.month
    table['day'] = table['datetime'].dt.day
    table = table[table['month'] == month]
    table1 = table.groupby(['date'], as_index=False).mean()
    table1['value'] = round(table1['value'], 0)
    # them ngay khong co vao table
    listDays = [*range(1, 32)]
    for i in table1.index:
        if table1.loc[i, 'day'] in listDays:
            listDays.remove(table1.loc[i, 'day'])
            # for j in listHours:
            #    list1 = [[j,0]]
    newList = []
    for j in listDays:
        newList.append([j, 0])
    df = pd.DataFrame(newList, columns=['day', 'value'])
    table1 = pd.concat([table1, df], ignore_index=True)
    table1.sort_values(by='day', inplace=True)
    # print(table1)
    listTime = []
    for i in table1['day'].tolist():
        listTime.append(int(float(str(i))))
    listValue = table1['value'].tolist()
    return listTime, listValue


def getDataByIdMonthly(idMachine, idSensor, year):
    electricalDataList = electrical.query.filter_by(idMachine_id=idMachine).all()
    listTime = []
    listValue = []
    data = {
        'timestamp': listTime,
        'value': listValue,
    }
    for electricalData in electricalDataList:
        listTime.append(electricalData.__dict__['time'])
        listValue.append(electricalData.__dict__[idSensor])
    table = pd.DataFrame(data)
    # loc  dataframe
    table.sort_values(by='timestamp', inplace=True)
    table.drop_duplicates(subset='timestamp', inplace=True)
    table['timestamp'] //= 1000
    table['datetime'] = pd.to_datetime(table['timestamp'], unit='s')
    table['year'] = table['datetime'].dt.year
    table['month'] = table['datetime'].dt.month
    table = table[table['year'] == year]
    table1 = table.groupby(['year', 'month'], as_index=False).mean()
    table1['value'] = round(table1['value'], 0)
    listMonths = [*range(1, 13)]
    for i in table1.index:
        if table1.loc[i, 'month'] in listMonths:
            listMonths.remove(table1.loc[i, 'month'])
            # for j in listHours:
            #    list1 = [[j,0]]
    newList = []
    for j in listMonths:
        newList.append([j, 0])
    df = pd.DataFrame(newList, columns=['month', 'value'])
    table1 = pd.concat([table1, df], ignore_index=True)
    table1.sort_values(by='month', inplace=True)
    # print(table1)
    listTime = []
    for i in table1['month'].tolist():
        listTime.append(int(float(str(i))))
    listValue = table1['value'].tolist()
    return listTime, listValue


if __name__ == '__main__':
    a, b =getDataByIdHourly("g13", 'eleewh', 11)
    #a, b = getDataByIdMonthly("g13", 'eleewh', 2022)
    # getEnergyByIdDaily()
    print(a)
    print(b)
