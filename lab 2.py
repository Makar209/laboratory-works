import requests

city = "Moscow, RU"
appid = "fd10e3819f04b731074a39f329b73d3b"
resOnToDay = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru','APPID': appid,})
dataOnToday = resOnToDay.json()
#Прогноз погоды на день
print("Прогноз погоды на день")
print("Город:", city)
print("Погодные условия:", dataOnToday['weather'][0]['description'])
print("Температура:", dataOnToday['main']['temp'])
print("Минимальная температура:", dataOnToday['main']['temp_min'])
print("Максимальная температура", dataOnToday['main']['temp_max'])
print("____________________________")


resOnWeek = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru','APPID': appid,})
dataOnWeek = resOnWeek.json()

#Прогноз погоды на неделю
print("Прогноз погоды на неделю:")
for i in dataOnWeek['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">")
print("____________________________")

#Задание для самостоятельного решения:
#Вывести скорость ветра и видимость для текущего прогноза и для прогноза на неделю

print("Прогноз ветра и видимости на сегодня:")
print('Cкорость ветра: ', dataOnToday['wind']['speed'], ' м/с')
print("Видимость: ", (dataOnToday['visibility'] / 10000)*100, '%')
print('----------------------------------')

print("Прогноз ветра и видимости на неделю:")
for i in dataOnWeek["list"]:
    print("Дата: ", i['dt_txt'], 
    "\r\n Скорость ветра: ", i['wind']['speed'], ' м/с',
    "\r\n Видимость: ", round((i['visibility'] / 10000)*100), '%')
