import telebot

bot = telebot.TeleBot('6005437532:AAFgaZpYzH83a8_NqJJCFpSIks8tscELsvI')


@bot.message_handler(commands=['start'])
# hi
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}{message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')



bot.polling(none_stop=True)
