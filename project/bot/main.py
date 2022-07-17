# import telebot
# from telebot import types
# from telebot.types import *
# 
# bot = telebot.TeleBot("5266261551:AAFmF1WZH6UONiuqMblxbSwsPAGKlRlnRe0")
# @bot.message_handler(commands=["start"])
# def send_welcome(message):
    # username = message.from_user.username
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton(text="🎞Kino🎞")
    # btn2 = types.KeyboardButton(text="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻")
    # btn3 = types.KeyboardButton(text="🎧🎵Musiqa🎧🎵")
    # keyboard.add(btn1,btn2,btn3)
    # bot.send_message(message.chat.id,f"Assalomu aleykum. {username}\n 🔊Ovoz_li🔊botimizga \n 🎉🎉Xush kelibsiz!!!🎉🎉!!! \n Sizni qiziqtirgan tugmani tanlang:",reply_markup=keyboard)
# 
# 
# @bot.message_handler(content_types=["text"])
# def start_text(message):
    # if message.text =="🎞Kino🎞":
        # keyboard = types.InlineKeyboardMarkup()
        # url1 = types.InlineKeyboardButton(text="Liga Adjustise 2021",url="https://t.me/Tudum_Netflix/247")
        # url2 = types.InlineKeyboardButton(text="Liga Adjustise 2017",url="https://t.me/Tudum_Netflix/245")
        # url3 = types.InlineKeyboardButton(text="Forsag 9",url="https://t.me/Tudum_Netflix/242")
        # url4 = types.InlineKeyboardButton(text="Infinity",url="https://t.me/Tudum_Netflix/234")
        # url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
        # keyboard.add(url1,url2,url3,url4,url5)
        # 
        # bot.send_message(message.chat.id,"Filmingizni tanlang:",reply_markup=keyboard)
    # 
# 
    # if message.text =="🅿️👩🏻‍💻Pycharm🅿️👩🏻‍💻":
        # keyboard = types.InlineKeyboardMarkup()
        # key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes')
        # keyboard.add(key_yes)
        # key_no = types.InlineKeyboardButton(text="No",callback_data='no')
        # keyboard.add(key_no)
# 
        # question = f"PyCharm-ni o'rnatmoqchimisiz?"
        # bot.send_message(message.from_user.id,text = question, reply_markup = keyboard)
        # 
        # 
            #    
    # if message.text =="🎧🎵Musiqa🎧🎵":
        # keyboard = types.InlineKeyboardMarkup()
        # url1 = types.InlineKeyboardButton(text="Bir necha musiqa",url="https://t.me/vkm_bot")
        # url2 = types.InlineKeyboardButton(text="Uzbek musiqalari",url="https://t.me/Uzbek_zakaz_music_qo_shiqlar")
        # url3 = types.InlineKeyboardButton(text="Arab musiqalari",url="https://t.me/bass_muzikil999")
        # url4 = types.InlineKeyboardButton(text="Rus musiqalari",url="https://t.me/russianmuiscnews")
        # url5 = types.InlineKeyboardButton(text="⬅⬅Menyuga qaytish",callback_data = "⬅⬅Orqaga")
        # keyboard.add(url1,url2,url3,url4,url5)
    # 
        # bot.send_message(message.chat.id,"Musiqangizni tanlang:",reply_markup=keyboard)
# 
# 
# @bot.callback_query_handler(func=lambda call:True)
# def get_call(call):
    # username = call.message.from_user.username
    # if call.data == "Orqaga":
        # send_welcome(call.message)
# 
    # if call.data== "yes": 
        # bot.send_message(call.message.chat.id,"https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows")
    # elif call.data== "no": 
        # bot.send_message(call.message.chat.id,f"Yana {username}, da ko'rishguncha..!!!✋🏻✋🏻✋🏻")
        # bot.register_next_step_handler(call.message,send_welcome)
# 
# bot.polling()








# import telebot
# from telebot.types import *
# 
# 
# bot = telebot.TeleBot("5113084134:AAE1Pm_3YzMYEwu0jKVEVUukLVzs4tEwLBs")
# 
# 
# 
# data = {
    # "user": {},
    # "admin": [],
    # "type": {}
    # 
# }
# 
# 
# 
# def get_keyboard():
    # return ReplyKeyboardMarkup(resize_keyboard=True).add(
        # KeyboardButton("Ro'yxatdan o'tish")
    # )
    # 
# 
# def get_inlinekeybord():
    # keyboard = InlineKeyboardButton(row_width=1)
    # first_name = InlineKeyboardButton("Ism", callback_data ="first_name+1")
    # last_name = InlineKeyboardButton("Familiya", callback_data="last_name+1")
    # phone = InlineKeyboardButton('Telefon nomer', callback_data="phone+1")
    # return keyboard.add(first_name, last_name, phone)
# 
# 
# def update_type(message):
    # user_id = message.chat.id
    # user_type = data['type'][user_id]
    # text = message.text
    # if user_type == 'phone':
        # if text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
            # data["user"][user_id][user_type] = message.text
            # bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
        # else:
            # bot.send_message(user_id, "Boshqatdan telefon nomerni  kiriting")
            # bot.register_next_step_handler(message, update_type)
    # else:
        # if text.isalpha():
            # data['user'][user_id][user_type] = message.text
            # bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
        # else:
            # type = {
                # "first_name": "Ism",
                # "last_name": "Familiya"
                # 
            # }
            # bot.send_message(user_id, f"Boshqatdan {type[user_type]} kiriting")
            # bot.register_next_step_handler(message, update_type)
# 
# @bot.callback_query_handler(func=lambda x: x.data.split("+")[-1] == "1")
# def update_user_data(call):
    # type_user = call.data.split("+")[0]
    # user_id = call.meassage.chat.id
    # data['type'][user_id] = type_user
    # type ={
        # "first_name": "Ism",
        # "last_name": "Familiya",
        # "phone": "Telefon nomer"
    # }
    # bot.edit_message_text(
        # f"{type[type_user]} kiriting",
        # call.message.chat.id,
        # call.message.id
    # )
    # 
    # bot.register_next_step_handler(call.message, update_type)
# 
# def data_text(message):
    # user_data = data["user"][message.chat.id]
    # if user_data:
        # text = f"Ism: {user_data['first_name']}\n" \
            #    f"Familiya: {user_data['last_name']}\n" \
            #    f"Telefon nomer: {user_data['phone']}\n"
        # return text
    # data["user"][message.chat.id] = {
        # "first_name": "-",
        # "last_name": "-",
        # "phone": "-"
    # }
    # return "Ism: -\n" \
        #    "Familiya: -\n" \
        #    "Telefon nomer: -"
# 
# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish")
# def registration(message):
    # text = data_text(message)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeybord())
    # 
# @bot.message_handler(commands="start")
# def start(message):
    # if message.chat.id not in data['user']:
        # data["user"][message.chat.id] = {}
    # bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())
# 
# bot.polling()
 

# Sinf ishi

# n = 12
# def ebo(n):
    # if n == 0:
        # return 0 
    # return n + ebo(n-1)
# print(ebo(12))


# a = int(input('son kiriting: '))
# def ebo(n):
    # if n == 0:
        # return 1
    # return n * ebo(n-1)
# 
# print(ebo(a))






# 
# def ebo():
    # print(123)
    # return ebo()
# 
# 
# print(ebo())


# n = 12
# def ebo(n):
    # if n == 0:
        # return 0 
    # return n + ebo(n-1)
# print(ebo(12))





# def dunyo(n):
    # return n
# 
# print(dunyo(123))






# def media(f):
    # def team():
        # s = f()
        # return s[::-1]
    # return team
# @media 
# def ebo():
    # return "salom"
# 
# 
# print(ebo()) 


# Recursiya--------> Funksiyani ichida funksiya ishlatishga aytiladi

#Decoratsiya-------> Print bilan Return orasidagi narsa. |
# Returndan Decoratorga jo'natadi.Decorator ishlab, ishlab printga jo'natadi.



# Decorator

# def media(f):
    # def team():
        # s = f()
        # return s[::-1]
    # return team
# @media 
# def ebo():
    # return "salom"
# 
# 
# 
# @media 
# def world():
    # return "dunyo"
# 
# 
# print(ebo()) 
# print(world())






        




# import telebot
# from telebot.types import *


# bot = telebot.TeleBot("5113084134:AAE1Pm_3YzMYEwu0jKVEVUukLVzs4tEwLBs")



# data = {
#     "user": {},
#     "admin": [895752511],
#     "type": {}
    
# }



# def get_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxatdan o'tish")
#     )
    

# def get_inlinekeybord():
#     keyboard = InlineKeyboardButton(row_width=1)
#     first_name = InlineKeyboardButton("Ism", callback_data ="first_name+1")
#     last_name = InlineKeyboardButton("Familiya", callback_data="last_name+1")
#     phone = InlineKeyboardButton('Telefon nomer', callback_data="phone+1")
#     return keyboard.add(first_name, last_name, phone)


# def update_type(message):
#     user_id = message.chat.id
#     user_type = data['type'][user_id]
#     text = message.text
#     if user_type == 'phone':
#         if text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
#             data["user"][user_id][user_type] = message.text
#             bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
#         else:
#             bot.send_message(user_id, "Boshqatdan telefon nomerni  kiriting")
#             bot.register_next_step_handler(message, update_type)
#     else:
#         if text.isalpha():
#             data['user'][user_id][user_type] = message.text
#             bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
#         else:
#             type = {
#                 "first_name": "Ism",
#                 "last_name": "Familiya"
                
#             }
#             bot.send_message(user_id, f"Boshqatdan {type[user_type]} kiriting")
#             bot.register_next_step_handler(message, update_type)

# @bot.callback_query_handler(func=lambda x: x.data.split("+")[-1] == "1")
# def update_user_data(call):
#     type_user = call.data.split("+")[0]
#     user_id = call.meassage.chat.id
#     data['type'][user_id] = type_user
#     type ={
#         "first_name": "Ism",
#         "last_name": "Familiya",
#         "phone": "Telefon nomer"
#     }
#     bot.edit_message_text(
#         f"{type[type_user]} kiriting",
#         call.message.chat.id,
#         call.message.id
#     )
    
#     bot.register_next_step_handler(call.message, update_type)

# def data_text(message):
#     user_data = data["user"][message.chat.id]
#     if user_data:
#         text = f"Ism: {user_data['first_name']}\n" \
#                f"Familiya: {user_data['last_name']}\n" \
#                f"Telefon nomer: {user_data['phone']}\n"
#         return text
#     data["user"][message.chat.id] = {
#         "first_name": "-",
#         "last_name": "-",
#         "phone": "-"
#     }
#     return "Ism: -\n" \
#            "Familiya: -\n" \
#            "Telefon nomer: -"

# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish")
# def registration(message):
#     text = data_text(message)
#     bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeybord())
    
# @bot.message_handler(commands="start")
# def start(message):
#     print(message.chat.id)
#     if message.chat.id in data["admin"]:
#         bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=admin_keyboard())
        
#     else:
#         if message.chat.id not in data['user']:
#             data["user"][message.chat.id] = {}
#     bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())




# def admin_keyboard():
#     return ReplyKeyboardMarkup(resize_keyboard=True).add(
#         KeyboardButton("Ro'yxat")
#     )


# bot.polling()










#    29.01.2021 yil
# Mavzu : OOP



# from math import *
# def shar_yuzi(r):
#     return 4 * pi * r ** 2


# def shar_hajmi(r):
#     return 4 / 3 * pi * r ** 3

# def kub_yuzi(a):
#     return 6 * a ** 3

# def kub_hajmi(a):
#     return a ** 3

# print(shar_yuzi(4), shar_hajmi(4))

# class Shar:
#     def __init__(self, r):
#         self.r = r
        
#     def yuza(self):
#         return 4 * pi  * self.r ** 2

#     def hajm(self):
#         return 4 / 3 * pi * self.r ** 3
    
#     def radius(self):
#         return self.r
    

# shar1 = Shar(4)
# shar2 = Shar(8)
# shar3 = Shar(29)

# print(shar1.yuza(), shar2.yuza(), shar3.hajm())
# print(shar1.hajm(), shar2.hajm(), shar3.hajm())


# from math import *
# class Tort:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
        
#     def yuza(self):
#         return self.a * self.b
    
#     def perimetr(self):
#         return 2 * (self.a + self.b) 
    
#     def diogonal(self):
#         return sqrt((self.a + self.b) ** 2 - 2 * self.a * self.b) 


# tort1 = Tort(12, 3)
# tort2 = Tort(2, 4)
# tort3 = Tort(5, 1)

# print(tort1.yuza(), tort2.diogonal(), tort3.perimetr())



# class Paralelipiped :
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def yuza(self):
#         return 2 * (self.a * self.b + self.c + self.b * self.c)
    
#     def hajm(self):
#         return self.a * self.b * self.c
    
    
#     def asos_perimetri(self):
#         return 2 *  (self.a + self.b)
        
        
#     def perimetr(self):
#         return 4 * (self.a + self.b)
        
# paralelipiped = Paralelipiped(5, 5, 9)
# paralelipiped = Paralelipiped(2, 9, 7)
# paralelipiped = Paralelipiped(3, 7, 6)

# print(paralelipiped.yuza(), paralelipiped.hajm(), paralelipiped.asos_perimetri())



