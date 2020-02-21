import telebot
import parser

#main variables
TOKEN = "788598180:AAEh9Xb_N_Z5t92F9zDJAnq2bP_qcefsoy4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()