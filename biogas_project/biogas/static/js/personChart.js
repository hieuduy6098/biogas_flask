$(document).ready(function(){


    $('#reloadPower').click(function(){
        $.ajax({
            url: '/chartPerson',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                "typeMessage": "reloadPower",
                "idMachine": idMachine,
                "typeChart": "elepwt",
                "month": new Date($("#selectMonthPower").val()).getMonth() + 1,
            }),
            contentType:"application/json; charset=UTF-8"
        }).done(function(data) {
            //console.log(data.value);
            labels3.length = 0;
            dataRealTime3.datasets[0].data.length = 0;
            data.time.forEach(function(element){
                labels3.push(element);
            });
            data.value.forEach(function(element){
                dataRealTime3.datasets[0].data.push(element);
            });
            //console.log(labels3);
            //console.log(dataRealTime3.datasets[0].data);
            myChart3.update();
        })
    })


    $('#dailyEnergyBtn').click(function(){
        $.ajax({
            url: '/chartPerson',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                "typeMessage": "dailyEnergy",
                "idMachine": idMachine,
                "typeChart": "eleewh",
                "month": new Date($("#selectMonthEnergy").val()).getMonth() + 1,
            }),
            contentType:"application/json; charset=UTF-8"
        }).done(function(data) {
            //console.log(data.value);
            labels4.length = 0;
            dataRealTime4.datasets[0].data.length = 0;
            data.time.forEach(function(element){
                labels4.push(element);
            });
            data.value.forEach(function(element){
                dataRealTime4.datasets[0].data.push(element);
            });
            //console.log(labels4);
            //console.log(dataRealTime4.datasets[0].data);
            myChart4.update();
        })
    })

    $('#monthlyEnergyBtn').click(function(){
        $.ajax({
            url: '/chartPerson',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                "typeMessage": "monthlyEnergy",
                "idMachine": idMachine,
                "typeChart": "eleewh",
                "year": new Date($("#selectMonthEnergy").val()).getFullYear(),
            }),
            contentType:"application/json; charset=UTF-8"
        }).done(function(data) {
            //console.log(data.value);
            labels4.length = 0;
            dataRealTime4.datasets[0].data.length = 0;
            data.time.forEach(function(element){
                labels4.push(element);
            });
            data.value.forEach(function(element){
                dataRealTime4.datasets[0].data.push(element);
            });
            config4.options.scales.x.title.text = "Tháng";
            //console.log(labels4);
            //console.log(dataRealTime4.datasets[0].data);
            myChart4.update();
        })
    })
})