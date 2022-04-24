#!/usr/bin/env python3

from time import sleep
import telebot

bot = telebot.TeleBot('5360100466:AAEDFZb5dYD5G7KqJ1lojz2vERSv8a4E-v4')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введи, пожалуйста, своё \
<b>имя</b>', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Катя":
        bot.send_message(message.chat.id, "Я люблю тебя!")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAE\
EiqRiYxD0dcWwibZDUi10lVxqIyrq-gACzAQAAhyS0gMM4Xbjastl2iQE")
    elif message.text == "Стас":
        bot.send_message(message.chat.id, "Здарова Стасян ХДДДД")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAE\
EiqZiYxE6t0puVGwNU7I0sqtmPDqyFwACBQADeIbbPQEpc8j1HT-2JAQ")
    elif message.text == "Данил":
        bot.send_message(message.chat.id, "Даня привет 😳")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAE\
EiqZiYxE6t0puVGwNU7I0sqtmPDqyFwACBQADeIbbPQEpc8j1HT-2JAQ")
    else:
        bot.send_message(message.chat.id, "Я ниче не понял.....")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAE\
EiqJiYxCE7JNaJmpHBowng-irugg4zgACGwoAAk2N0EkeWjg1iHogKCQE")
        time.sleep(2)
        bot.send_message(message.chat.id, "...")
        sleep(2)
        bot.send_message(message.chat.id, "....")
        sleep(2)
        bot.send_message(message.chat.id, "Иди нахуй, короче.")


bot.polling(none_stop=True)
