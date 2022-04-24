from time import sleep
import telebot

bot = telebot.TeleBot('5321282908:AAGuTGeVp-5cjHL_gZNaRvrDLNCnBFGZCco')


@bot.message_handler()
def get_user_text(message):
	sleep(5)
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)