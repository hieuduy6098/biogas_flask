// when click button call function publish from connectMqtt.js
$(document).ready(function () {
    $("#submit").click(function () {
        var location = $("form select option:selected").val();          //g01 or g02 or g03 or g04
        var param_id = $("form input[type='radio']:checked").val();     //elexx or envxx
        var time_begin = new Date($("#time_begin").val()).getTime();    //time (milisecond)        
        var time_end = new Date($("#time_end").val()).getTime();        //time (milisecond)        
        //console.log(location, param_id, time_begin, time_end); 
        // at the moment it is not allowed to load more than 30 minute data
        // max_duration = 1800000; // in miliseconds = 30 minutes 
        max_duration = 3600000; // in miliseconds = 60 minutes 
        
        var is_valid_duration = true;
        
        if (isNaN(time_end)) {
            if (isNaN(time_begin)){
                var currenttime = new Date().getTime();
                time_end = currenttime;
                time_begin = time_end - max_duration;
            }
            else {
                time_end = time_begin + max_duration;
            }
        }
        else {
            if (isNaN(time_begin)){
                time_begin = time_end - max_duration;
            }
            else{
                if ((time_end - time_begin) > max_duration) {
                    time_begin = time_end - max_duration;
                }
                else if ((time_end - time_begin) < 0) {
                    console.log("invalid");
                    is_valid_duration = false;
                }
            }
        }
  
        if (param_id == undefined) {
            alert("please select type sensor");
            is_valid_duration = false;
        }
  
        // console.log(location,location+param_id,time_begin,time_end);
        if (is_valid_duration) {     
            publish(location, location+param_id, time_begin, time_end); 
        }            
    })
  });
  