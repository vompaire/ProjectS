import telebot
import requests
import json
import re
from config import keys, bot, payload, headers


class AllExc(Exception):
    pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"для работоспособности введите в формате <имя валюты, цену которой хочется знать>, <имя валюты, которую хочется перевести>, <колво переводимой валюты> Вводить в имменительном падеже. пример: Доллар рУбль 101, узнать доступные валюты /values")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    val = "валюты:"
    for key in keys.keys():
        val = '\n'.join((val, key,))
    bot.send_message(message.chat.id, val)


@bot.message_handler(content_types=["text"])
def start(message: telebot.types.Message):
    try:
        val = message.text.split(" ")
        if len(val) != 3:
            raise AllExc("Неправильный ввод даных, введите /help для помощи")
        qoute, base, amount = val
        if qoute.lower() == base.lower():
            raise AllExc("Невозможно конвертировать одиннаковые валюты")
        try:
            float(amount) == False
        except ValueError:
            raise AllExc("Введите число")
        if float(amount) <= 0:
            raise AllExc("введите натуральное число")
        if qoute.lower() not in keys or base.lower() not in keys:
            raise AllExc("такой валюты нету, посмотрите /values какие есть")
        response = requests.request("GET", url=f"https://api.apilayer.com/exchangerates_data/convert?to={keys[qoute.lower()]}&from={keys[base.lower()]}&amount={amount}", headers=headers, data=payload)
    except Exception as e:
        bot.reply_to(message, f"Ошибка со стороны пользователя\n{e}")
    except AllExc as e:
        bot.reply_to(message, f"Ошибка у бота \n{e}")
    else:
        response = json.loads(response.content)
        bot.reply_to(message, f"{amount} {base} это {'{:.10f}'.format(float(response['result'])).rstrip('0').rstrip('.')} {qoute}")



bot.polling(none_stop=True)
