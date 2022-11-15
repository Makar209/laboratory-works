'use strict'

let now = new Date(); // сегодняшняя дата
let day = now.getDate();
function toDayDateMY() {
    return '.' + now.getMonth() + '.' + now.getFullYear();
}

function weatherDailyRequest(){
    let appidKey = '1ae615866648f086a286c190283e6b0c';
    let UrlDaily = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=' + appidKey + '&units=metric&lang=ru';
    document.getElementById('turn4').innerHTML = '';

    let xhrForDailyRequest = new XMLHttpRequest();
    
    xhrForDailyRequest.open('GET', `${UrlDaily}`);
    
    xhrForDailyRequest.send();
    
    xhrForDailyRequest.responseType = 'json';
    
    xhrForDailyRequest.onload = function () {
        let dailyResponseObj = xhrForDailyRequest.response;
        document.getElementById('turn0').innerHTML = 'Oбщее описание погоды: ' + upWord(dailyResponseObj['weather'][0]['description']);
        document.getElementById('turn1').innerHTML = 'Температура воздуха сейчас: ' + Math.round( dailyResponseObj['main']['temp'] ) + '°';
        document.getElementById('turn2').innerHTML = 'Ощущается как: ' + Math.round( dailyResponseObj['main']['feels_like'])  + '°';
        document.getElementById('turn3').innerHTML = 'Направление ветра: ' + directionWind(Math.round(dailyResponseObj['wind']['deg']));
        document.getElementById('turn40').innerHTML = 'Максимальная температура: ' + Math.round( dailyResponseObj['main']['temp_max'] ) + '°';
        document.getElementById('turn5').innerHTML = 'Минимальная температура: ' + Math.round( dailyResponseObj['main']['temp_min'] ) + '°';
        document.getElementById('turn6').innerHTML = 'Видимость: ' + visToProc( dailyResponseObj['visibility'] ) + ' %';
        document.getElementById('turn7').innerHTML = 'Скорость ветра: ' +  Math.round(dailyResponseObj['wind']['speed']) + ' м/c';
    } 
}
function weatherRequest(){
    let appidKey = '1ae615866648f086a286c190283e6b0c';
    let UrlForWeek = 'https://api.openweathermap.org/data/2.5/forecast?q=Moscow&appid=' + appidKey + '&units=metric&lang=ru&cnt=40';
    
    let xhrForWeekRequest = new XMLHttpRequest();
    
    xhrForWeekRequest.open('GET', `${UrlForWeek}`);
    
    xhrForWeekRequest.send();
    
    xhrForWeekRequest.responseType = 'json';
    xhrForWeekRequest.onload = function () {
        document.getElementById('turn40').innerHTML = '';
        document.getElementById('turn5').innerHTML = '';
        document.getElementById('turn6').innerHTML = '';
        document.getElementById('turn7').innerHTML = '';
        let weekResponseObj = xhrForWeekRequest.response;
        let lisId = 0;
        let idDoc = '';
        for(let i = 0; i <= 5; i++) {
            idDoc = 'turn' + i;
            document.getElementById(idDoc).innerHTML = 'Дата: ' + String(day + i) + toDayDateMY() + ' Температура: ' 
            + Math.round(weekResponseObj['list'][lisId]['main']['temp']) + '°';
            lisId += 8;
        }
        
    } 
}


//Функции для обработки результатов
function visToProc(vis) {
    return Math.round(vis / 10000) * 100
}
function directionWind(deg) {
    if ( ( (deg >= 0) && (deg <= 45) ) || ( (deg >= 315) && (deg <= 360) ) ) {
        return 'Северное';
    }
    if ( (deg > 45) && (deg <= 135) ) {
        return 'Восточное';
    }
    if ( (deg > 135) && (deg <= 225) ) {
        return 'Южное';
    }
    if ( (deg > 225) && (deg < 315) ) {
        return 'Западное';
    }
};
function upWord(str) {
    let upW = str[0].toUpperCase(); 
    for (let i = 1; i < str.length; i++) {
        upW += str[i];
    }
    return upW;
};



