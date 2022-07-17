# print('Assalomu aleykum')
# print("Qaysi viloyatni tanlaysiz")
# ism = input("ismingiz")
# print("1 - BUXORO")
# print("2 - TOSKENT")
# a = int(input("nechinchi viloyatni tanladingiz"))
# if a == 1:
#     print("SIZ BUXORONI TANLADINGIZ")
#     print("LAYLAK")
#     print("ZARANGARI")
#     b = int(input("TUMANNI TANLANG"))
#     if b == 1:
#         print("LAYLAKKA Xush kelibsiz")
#         print("xato")




import telebot
from telebot.types import *
bot = telebot.Telebot("5001242758:AAHNwPgdlNzbH8k6cwdxKMdLb_qnmSri4iM")
def mirza(message):
    text = len(message.text)
    bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
def shrine(message):
    if message.text == "Mirza":
        bot.send_message(message.chat.id, "soz yozing", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, mirza)
    elif message.text == "Ulugbek":
        bot.send_message(message.chat.id, "2")
        bot.register_next_step_handler(message, shrine)
    elif message.text == "Temuriy":
        bot.send_message(message.chat.id, "3")
        bot.register_next_step_handler(message, shrine)
    else:
        bot.send_message(message.chat.id, "4")
        bot.register_next_step_handler(message, shrine)
def get_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    btn1 = KeyboardButton("Mirza")
    btn2 = KeyboardButton("Ulugbek")
    btn3 = KeyboardButton("Temuriy")
    keyboard.add(btn1,btn2,btn3)
    return keyboard
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "salom", reply_markup=get_keyboard())
    bot.register_next_step_handler(message, shrine)
bot.polling()