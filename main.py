import telebot
import logging
from telebot import types
#from aiogram import Bot, Dispatcher, executor, types

bot = telebot.TeleBot('6005437532:AAFgaZpYzH83a8_NqJJCFpSIks8tscELsvI')

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Отправить текст'),types.KeyboardButton('Отправить аудио'))
    keyboard.add(types.KeyboardButton('Ответы на вопросы'))
    bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}</b> ! Вас приветствует телеграм бот , которий преобразовывает аудио дорожки в текст и наоборот', parse_mode='html', reply_markup=keyboard)
    bot.send_message(message.chat.id, f'Cегодня мы будем тестировать мои функции')
    bot.send_message(message.chat.id, f'Cделайте свой выбор , как вы хотите преобразовать текст')

#@bot.message_handler(contetn_types=['text'])
#def main_menu(message):
#    if message.text == 'Отправить текст'
#        bot.send_message(message.chat.id,  =)


bot.polling(none_stop=True)
