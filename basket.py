from telebot import types
import telebot
import time 

# Ваш токен API Telegram
TOKEN = '6656804610:AAGgmMrFmv4HU_EYTUWPWzNlmL9srdg4iWs'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, "Привет! Отправь мне  '🏀', чтобы сыграть в баскетбол!")


@bot.message_handler(content_types=['dice'])
def dice_value(message):
    value = message.dice.value
    if value == 5 or value == 4:
        time.sleep(3)
        bot.send_message(message.chat.id, 'Вы выиграли')
    else:
        time.sleep(3)
        bot.send_message(message.chat.id, 'Вы проиграли')
        





        




bot.polling()