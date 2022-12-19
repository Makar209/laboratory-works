import telebot
from telebot import types
import requests
import psycopg2
import datetime


week_number = datetime.datetime.today().isocalendar()[1] - 34 # Количество недель с января по сентябрь
weekischet = (week_number % 2) == 0
now = datetime.datetime.now()
weekday = datetime.datetime.weekday(now)


def whatIsTheDay(numb):
    if numb == 0:
        return "Понедельник"
    if numb == 1:
        return "Вторник"
    if numb == 2:
        return "Среда"
    if numb == 3:
        return "Четверг"
    if numb == 4:
        return "Пятница"
    if numb == 5:
        return "Cyббота"
    if numb == 6:
        return "Воскресенье"


conn = psycopg2.connect(
    database="timetable",
    user="postgres",
    password="1703",
    host="localhost",
    port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM timetable")
records = list(cursor.fetchall())


token = "5954286172:AAEKO57KUwFHi2B2B5SNYWvHmRA0NDvZzXw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/today", "/week", "/nextweek")
    bot.send_message(
        message.chat.id, 'Привет! Это бот с расписанием группы БИН2206', reply_markup=keyboard)


@bot.message_handler(commands=['today'])
def today(message):
    if weekday == 5 or weekday == 6:
        bot.send_message(
            message.chat.id, "Сегодня выходной!")
    else: 
        table = f'{whatIsTheDay(weekday)}\n--------'
        if weekischet: 
            for i in range((weekday * 5), (weekday * 5) + 5):
                if records[i][2] == None:
                        table += '\nОкно\n----------'
                else:
                    table += f"\nПредмет: {records[i][2]}\nКабинет: {records[i][3]}\nВремя: {records[i][4]}\nПреводаватель: {records[i][5]}\n----------"
            bot.send_message(
                message.chat.id, f'{table}')
        else:
            for i in range((weekday * 5 + 25), (weekday * 5) + 5 + 25):
                if records[i][2] == None:
                        table += '\nОкно\n----------'
                else:
                    table += f"\nПредмет: {records[i][2]}\nКабинет: {records[i][3]}\nВремя: {records[i][4]}\nПреводаватель: {records[i][5]}\n----------"
            bot.send_message(
                message.chat.id, f'{table}')


@bot.message_handler(commands=['week'])
def week(message):
    def createTableWeek(start, end):
        nDay = 0
        for g in range(start, end):
            table = f'{whatIsTheDay(weekday + nDay)}\n----------'
            for i in range(g * 5, ((g * 5) + 5)):
                if records[i][2] == None:
                    table += '\nОкно\n----------'
                else:
                    table += f"\nПредмет: {records[i][2]}\nКабинет: {records[i][3]}\nВремя: {records[i][4]}\nПреводаватель: {records[i][5]}\n----------"
            bot.send_message(
                message.chat.id, f'{table}')
            nDay += 1

    if weekischet:
        createTableWeek(0, 5)
    else:
        createTableWeek(5, 10)

@bot.message_handler(commands=['nextweek'])
def nextweek(message):
    def createTableWeek(start, end):
        nDay = 0
        for g in range(start, end):
            table = f'{whatIsTheDay(weekday + nDay)}\n----------'
            for i in range(g * 5, ((g * 5) + 5)):
                if records[i][2] == None:
                    table += '\nОкно\n----------'
                else:
                    table += f"\nПредмет: {records[i][2]}\nКабинет: {records[i][3]}\nВремя: {records[i][4]}\nПреводаватель: {records[i][5]}\n----------"
            bot.send_message(
                message.chat.id, f'{table}')
            nDay += 1

    if weekischet == False:
        createTableWeek(0, 5)
    else:
        createTableWeek(5, 10)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Все просто: \n/today - расписание на сегодня\n/week - рассписание текущую на неделю\n/nextweek - расписание на след неделю\nПросто нажми соответствующие кнопки!')


bot.polling(none_stop=True, interval=0)

