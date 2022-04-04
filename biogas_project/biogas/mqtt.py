from paho.mqtt import client as mqtt_client
import json
from biogas import db
from model import *

#infor mqtt broker
broker = '27.71.227.145'
port = 1883
topic = "sensor_data"
client_id = 'publicDcs1'
username = ''
password = ''

#connect mqtt
def connect_mqtt():
  def on_connect(client, userdata, flags, rc):
    if rc == 0:
      print("Connected to MQTT Broker!")
    else:
      print("Failed to connect, return code %d\n", rc)

  client = mqtt_client.Client(client_id)
  client.username_pw_set(username, password)
  client.on_connect = on_connect
  client.connect(broker, port)
  return client

# sub from mqtt
def subscribe(client: mqtt_client):
  def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode())
    # get message and insert to db
    if message['type'] == 'environment':
      dictData = {}
      for item in message['data']:
        dictData[item['id'][3:]] = item['v']
      #insert data to db
      try:
        data = environment(
          idMachine_id=message['rpi'],
          time=message['time'],
          envtw=dictData['envtw'],
          envpo=dictData['envpo'],
          envo2=dictData['envo2'],
          envh2s=dictData['envh2s']
        )
        db.session.add(data)
        db.session.commit()
      except:
        print('error to insert environment')
    elif message['type'] == 'electrical':
      dictData = {}
      for item in message['data']:
        dictData[item['id'][3:]] = item['v']
      # insert data to db
      try:
        data = electrical(
          idMachine_id=message['rpi'],
          time=message['time'],
          eles=dictData['eles'],
          eleva =dictData['eles'],
          elevb =dictData['elevb'],
          elevc = dictData['elevc'],
          elevna = dictData['elevna'],
          elevab = dictData['elevab'],
          elevbc = dictData['elevbc'],
          elevca = dictData['elevca'],
          elevla = dictData['elevla'],
          eleia = dictData['eleia'],
          eleib = dictData['eleib'],
          eleic = dictData['eleic'],
          eleiav = dictData['eleiav'],
          elepwa = dictData['elepwa'],
          elepwb = dictData['elepwb'],
          elepwc = dictData['elepwc'],
          elepwt = dictData['elepwt'],
          elepfa = dictData['elepfa'],
          elepfb = dictData['elepfb'],
          elepfc = dictData['elepfc'],
          elepft = dictData['elepft'],
          elef = dictData['elef'],
          eleewh = dictData['eleewh'],
          eleevah = dictData['eleevah'],
          eletop = dictData['eletop'],
          elethdva = dictData['elethdva'],
          elethdvb = dictData['elethdvb'],
          elethdvc = dictData['elethdvc'],
          elethdia = dictData['elethdia'],
          elethdib = dictData['elethdib'],
          elethdic = dictData['elethdic'],
        )
        db.session.add(data)
        db.session.commit()
      except:
        print('error to insert electrical')
    elif message['type'] == 'operation':
      dictData = {}
      for item in message['data']:
        dictData[item['id'][3:]] = item['v']
      # insert data to db
      try:
        data = operation(
          idMachine_id=message['rpi'],
          time=message['time'],
          opete=dictData['opete'],
          opetb=dictData['opetb'],
          opepidsp=dictData['opepidsp'],
          opepidout=dictData['opepidout'],
          opevpb=dictData['opevpb'],
          opepb=dictData['opepb'],
          opevsfb=dictData['opevsfb'],
        )
        db.session.add(data)
        db.session.commit()
      except:
        print('error to insert operation')

  client.subscribe(topic)
  client.on_message = on_message

# function connect and get data from topic
def contactMqtt():
  client = connect_mqtt()
  subscribe(client)
  client.loop_forever()

if __name__ == '__main__':
    contactMqtt()
