from model import *
import pandas as pd
from datetime import datetime

def getDataByIdDaily(idMachine, idSensor, month):
    electricalDataList = electrical.query.filter_by(idMachine_id = idMachine).all()
    listTime = []
    listValue = []
    data = {
        'timestamp' : listTime,
        'value' : listValue,
    }
    for electricalData in electricalDataList:
        listTime.append(electricalData.__dict__['time'])
        listValue.append(electricalData.__dict__[idSensor])
    table = pd.DataFrame(data)
    #loc  dataframe
    table.sort_values(by='timestamp', inplace=True)
    table.drop_duplicates(subset='timestamp', inplace=True)
    table['timestamp'] //= 1000
    table['datetime'] = pd.to_datetime(table['timestamp'], unit='s')
    table['date'] = table['datetime'].dt.date
    table['month'] = table['datetime'].dt.month
    table['day'] = table['datetime'].dt.day
    table = table[table['month'] == month]
    table1 = table.groupby(['date'], as_index=False).mean()
    table1['value'] = round(table1['value'], 2)
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
    #print(table1)
    listTime = []
    for i in table1['day'].tolist():
        listTime.append(int(float(str(i))))
    listValue = table1['value'].tolist()
    return listTime, listValue
if __name__ == '__main__':
    timePowerData, valuePowerData = getDataByIdDaily("g13", 'elepwt', 4)
    print(timePowerData)
    print(valuePowerData)