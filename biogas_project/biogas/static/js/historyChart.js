$(document).ready(function(){
    $('#historySubmit').click(function(){
        $.ajax({
            url: '/chart',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                "idMachine": idMachine,
                "sensor": $('#listSensorHistory').val(),
                "start": new Date($("#startTime").val()).getTime(),
                "end": new Date($("#endTime").val()).getTime(),
            }),
            contentType:"application/json; charset=UTF-8"
        }).done(function(data) {
            console.log(data)
        })
    })
})