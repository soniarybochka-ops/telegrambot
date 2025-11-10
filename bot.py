import telebot
bot = telebot.TeleBot("8493969131:AAFkZdfkTCt3VRj9HimS233SQYMzEfX6WrE")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я S1gmaBot. Напиши что-нибудь!")    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)    
bot.polling()