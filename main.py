import telebot

bot = telebot.TeleBot('6005437532:AAFgaZpYzH83a8_NqJJCFpSIks8tscELsvI')


@bot.message_handler(commands=['start'])
# hi
def start(message):
    bot.send_message(message.chat.id, '<b> Привет :)</b>', parse_mode='html')


bot.polling(none_stop=True)
