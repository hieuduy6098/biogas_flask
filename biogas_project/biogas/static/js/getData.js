function updateGuiRealTimeValue(name, rpi, value, unit){
    //var doc_element = document.getElementById(rpi+"Ia");
    var doc_element = document.getElementById(rpi+name);
    //If it isn't "undefined" and it isn't "null", then it exists.
    if(typeof(doc_element) != 'undefined' && doc_element != null){
        document.getElementById(rpi+name).innerHTML = value + unit;
    } 
}

// function add data electrical to html
function getDataElectrical(data, rpi) {
    data.forEach(element => {
        var temp_id = element.id;
        temp_id = temp_id.replace(rpi,'');
        switch (temp_id) {
            case "eles":
                updateGuiRealTimeValue("eles", rpi, element.v, " vòng/phút");
                break;
            case "eleva":
                updateGuiRealTimeValue("eleva", rpi, element.v, " V");
                break;
            case "elevb":
                updateGuiRealTimeValue("elevb", rpi, element.v, " V");
                break;
            case "elevc":
                updateGuiRealTimeValue("elevc", rpi, element.v, " V");
                break;
            case "elevna":
                updateGuiRealTimeValue("elevna", rpi, element.v, " V");
                break;
            case "elevab":
                updateGuiRealTimeValue("elevab", rpi, element.v, " V");
                break;
            case "elevbc":
                updateGuiRealTimeValue("elevbc", rpi, element.v, " V");
                break;
            case "elevca":
                updateGuiRealTimeValue("elevca", rpi, element.v, " V");
                break;
            case "elevla":
                updateGuiRealTimeValue("elevla", rpi, element.v, " V");
                break;
            case "eleia":
                updateGuiRealTimeValue("eleia", rpi, element.v, " A");
                break;
            case "eleib":
                updateGuiRealTimeValue("eleib", rpi, element.v, " A");
                break;
            case "eleic":
                updateGuiRealTimeValue("eleic", rpi, element.v, " A");
                break;
            case "eleiav":
                updateGuiRealTimeValue("eleiav", rpi, element.v, " A");
                break;
            case "elepwa":
                data = (element.v)/1000;
                data = data.toFixed(2);
                updateGuiRealTimeValue("elepwa", rpi, data, " kW");
                break;
            case "elepwb":
                data = (element.v)/1000;
                data = data.toFixed(2);
                updateGuiRealTimeValue("elepwb", rpi, data, " kW");
                break;
            case "elepwc":
                data = (element.v)/1000;
                data = data.toFixed(2);
                updateGuiRealTimeValue("elepwc", rpi, data, " kW");
                break;
            case "elepwt":
                data = (element.v)/1000;
                data = data.toFixed(2);
                updateGuiRealTimeValue("elepwt", rpi, data, " kW");
                break;
            case "elepfa":
                updateGuiRealTimeValue("elepfa", rpi, element.v, " ");
                break;
            case "elepfb":
                updateGuiRealTimeValue("elepfb", rpi, element.v, " ");
                break;
            case "elepfc":
                updateGuiRealTimeValue("elepfc", rpi, element.v, " ");
                break;
            case "elepft":
                updateGuiRealTimeValue("elepft", rpi, element.v, " ");
                break;
            case "elef":
                updateGuiRealTimeValue("elef", rpi, element.v, " Hz");
                break;
            case "eleewh":
                data = Math.floor((element.v)*100);  
                data /= 100;         
                updateGuiRealTimeValue("eleewh", rpi, data, " kWh");
                break;
            case "eleevah":
                data = Math.floor((element.v)*100);
                data /= 100;  
                updateGuiRealTimeValue("eleevah", rpi, data, " kVAh");
                break;
            case "eletop":
                data = Math.floor((element.v)*100);
                data /= 100;  
                updateGuiRealTimeValue("eletop", rpi, data, " h");
                break;
            case "elethdva":
                updateGuiRealTimeValue("elethdva", rpi, element.v, " %");
                break;
            case "elethdvb":
                updateGuiRealTimeValue("elethdvb", rpi, element.v, " %");
                break;
            case "elethdvc":
                updateGuiRealTimeValue("elethdvc", rpi, element.v, " %");
                break;
            case "elethdia":
                updateGuiRealTimeValue("elethdia", rpi, element.v, " %");
                break;
            case "elethdib":
                updateGuiRealTimeValue("elethdib", rpi, element.v, " %");
                break;
            case "elethdic":
                updateGuiRealTimeValue("elethdic", rpi, element.v, " %");
                break;                
        }
    });
}

// function add data environment to html
function getDataEvironment(data, rpi) {
    data.forEach(element => {
        var temp_id = element.id;
        temp_id = temp_id.replace(rpi,'');
        switch (temp_id) {
            case "envtw":
                updateGuiRealTimeValue("envtw", rpi, element.v, " ℃");
                break;
            case "envpo":
                updateGuiRealTimeValue("envpo", rpi, element.v, " Bar");
                break;
            case "envo2":
                updateGuiRealTimeValue("envo2", rpi, element.v, " lambpda");
                break;
            case "envh2s":
                if (element.v < 0) {
                    updateGuiRealTimeValue("envh2s", rpi, 50, " ppm");
                    break; 
                } else {
                    updateGuiRealTimeValue("envh2s", rpi, element.v, " ppm");
                    break;
                }

        }
    });
}

// function add data environment to html
function getDataOperation(data, rpi) {
    data.forEach(element => {
        var temp_id = element.id;
        temp_id = temp_id.replace(rpi,'');
        switch (temp_id) {
            case "opepidsp":
                updateGuiRealTimeValue("opepidsp", rpi, element.v, " rpm");
                break;
            case "opepidout":
                updateGuiRealTimeValue("opepidout", rpi, element.v, " %");
                break;
            case "opevpb":
                updateGuiRealTimeValue("opevpb", rpi, element.v, " ");
                break;  
            case "opepb":
                updateGuiRealTimeValue("opepb", rpi, element.v, " mm");
                break;  
            case "opevsfb":
                updateGuiRealTimeValue("opevsfb", rpi, element.v, " %");
                break;                
            case "opetb":
                var dateTimeStamp = new Date().getTime();
                var timeBeginTimeStamp = Number(element.v)
                var timeOperate = (dateTimeStamp - timeBeginTimeStamp)/1000>>0;
                var timeOperateH = timeOperate/3600>>0;
                var timeOperateM = (timeOperate%3600)/60>>0;
                var timeOperateS = (timeOperate%3600)%60;

                var operateTime = String(timeOperateH) +":"+ String(timeOperateM) +":"+ String(timeOperateS);
                var timeBegin = new Date(timeBeginTimeStamp);
                var timeBeginTime = timeBegin.toLocaleTimeString();
                var timeBeginDate = timeBegin.toLocaleDateString();
                //console.log(timeBeginDate);
                updateGuiRealTimeValue("daytb", rpi, timeBeginDate, "");
                updateGuiRealTimeValue("timetb", rpi, timeBeginTime, "")
                updateGuiRealTimeValue("op", rpi, operateTime, "")
                break;
        }
    });
}

// function create chart in chartView.html
function getChart(x, y, typeChart) {
    Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
    Chart.defaults.global.defaultFontColor = '#858796';
    //console.log(x);
    //console.log(y);
    var typeSensor = typeChart.slice(6);
    switch (typeSensor) {
        case "ia":
            typeSensor = "Ia";
            break;
        case "ib":
            typeSensor = "Ib";
            break;
        case "ic":
            typeSensor = "Ic";
            break;
        case "vab":
            typeSensor = "Vab";
            break;
        case "s":
            typeSensor = "speed";
            break;
        case "f":
            typeSensor = "frequency";
            break;
        case "tw":
            typeSensor = "temperature H2O";
            break;
        case "po":
            typeSensor = "pressure Oil";
            break;
        case "o2":
            typeSensor = "concentration O2";
            break;
        case "h2s":
            typeSensor = "concentration H2S";
            break;                       
    }
    var ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: y,
            datasets: [{
                label: typeSensor,
                data: x,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54,5, 235, 0.2)',
                    'rgba(255, 206, 12, 0.2)',
                    'rgba(75, 5, 15, 0.2)',
                    'rgba(153, 14, 5, 0.2)',
                    'rgba(255, 5, 64, 0.2)'
                ],
                borderColor: "red",
                //borderWidth: 0,
                pointBorderWidth:0.1,
                pointRadius:0,
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

// called when a message arrives
function onMessageArrived(message) {
    if(message) {
        try {
            var data = JSON.parse(message.payloadString);
            //console.log(data);
            var topic = message.destinationName;
            if (topic == "sensor_data") {
                // revise this piece of code later
                if (data.rpi == "g01") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    } 
                } else if (data.rpi == "g02") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    } 
                } else if (data.rpi == "g03") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                        console.log()
                    } 
                } else if(data.rpi == "g04") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g05") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g06") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g07") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g08") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g09") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g10") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g11") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g12") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g13") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g14") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g15") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g16") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    }
                } else if(data.rpi == "g99") {
                    if (data.type == "electrical") {
                        getDataElectrical(data.data, data.rpi)
                    } else if (data.type == "environment") {
                        getDataEvironment(data.data, data.rpi)
                    } else if (data.type == "operation") {
                        getDataOperation(data.data, data.rpi)
                    } 
                }

            }
            else if (topic == "client_response/history") {
                var x = new Array();
                var y = new Array();
                if (!Array.isArray(data.data) || !data.data.length) {
                  // array does not exist, is not an array, or is empty
                  // ⇒ do not attempt to process array
                  console.log("No data");
                }
                else {
                    data.data.forEach(element => {
                        //var time = new Date(element.t).getDay()+":"+new Date(element.t).getMonth()+":"+new Date(element.t).getFullYear()+":"+new Date(element.t).getHours()+":"+new Date(element.t).getMinutes()+":"+new Date(element.t).getSeconds();
                        var datetime = new Date(element.t);
                        //var time = datetime.toLocaleDateString() + " " + datetime.toLocaleTimeString();
                        var time = datetime.toLocaleString();
                        // console.log(time);
                        x.push(element.v);
                        y.push(time);
                    });
                    getChart(x, y, data.id);
                }
            }
        } catch(e) {
            console.log("no data request"); // error in the above string (in this case, yes)!
        }
    }
}

