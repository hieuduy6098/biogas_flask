// Create a client instance
//client = new Paho.MQTT.Client("localhost", 8083, "web_" + parseInt(Math.random() * 100, 10));
client = new Paho.MQTT.Client("27.71.227.145", 8083, "web_" + parseInt(Math.random() * 100, 10));
//client = new Paho.MQTT.Client("soldier.cloudmqtt.com", 35513, "web_" + parseInt(Math.random() * 100, 10));
// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;
/*
var options = {
  useSSL: true,
  userName: "dwwsgduh",
  password: "Vx99bs6ekT-4",
  onSuccess:onConnect,
  onFailure:doFail
}
*/
// connect the client
//client.connect(options);
client.connect({onSuccess:onConnect});
//called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription
  console.log("onConnect");
  client.subscribe("sensor_data");
  client.subscribe("client_response/history");
}

//publish function
function publish(location, typedata, time_begin, time_end) {
  var element = {
    "rpi":location,
    "param_id":typedata,
    "time_begin":time_begin, 
    "time_end":time_end
  };
  element = JSON.stringify(element);
  var message = new Paho.MQTT.Message(element);               //publish message
    message.destinationName = "client_request/history";
    //message.destinationName = "client_request/hello";
    //message.destinationName = "test";
    message.qos = 0;
    client.send(message);
}
function doFail(e){
  console.log(e);
}
// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}
