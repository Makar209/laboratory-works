'use strict'

let appidKey = 'fd10e3819f04b731074a39f329b73d3b';
let UrlDaily = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=fd10e3819f04b731074a39f329b73d3b&units=metric&lang=ru';
let UrlForWeek = 'https://api.openweathermap.org/data/2.5/forecast?q=Moscow&appid=fd10e3819f04b731074a39f329b73d3b&units=metric&lang=ru';

let xhrForDailyRequest = new XMLHttpRequest();
let xhrForWeekRequest = new XMLHttpRequest();

xhrForDailyRequest.open('GET', `${UrlDaily}`);
xhrForWeekRequest.open('GET', `${UrlForWeek}`);

xhrForDailyRequest.send();
xhrForWeekRequest.send();

xhrForDailyRequest.responseType = 'json';
xhrForWeekRequest.responseType = 'json';

xhrForDailyRequest.onload = function () {
    let dailyResponseObj = xhrForDailyRequest.response;
}

