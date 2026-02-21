import telebot 
from config import TOKEN
from logic import gen_pass 
import os
import random

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN)
memes = os.listdir("./image")


users = {}
decay = {"пластик":"до 1000 лет"}


# @bot.message_handler(command=['collection'])
# def send_collection(message):
#     #нужна папка с картинками для их выселения.
#     user = message.from_user.id
#     p = random.choice
#     if user not in users:  #если юзер не в козере
#         users[user] = []   #список

#     users[user].append(p)  #добавляется p (картинка рандом)


@bot.message_handler(commands=['nick'])
def send_nick(message):
    user_name = message.from_user.username
    words = message.text.split()
    if len(words) > 1:
        password = gen_pass(int(words[1]))
    else:
        password = gen_pass(8)
    bot.reply_to(message, f"Ваш новый ник: {user_name+password}")


@bot.message_handler(commands=["meme"])
def send_meme(message):
    words = message.text.split()
    if len(words) == 2:
        num_mem = int(words[1])
        if 0 < num_mem <= len(memes):
            with open(f"./image/{memes[num_mem - 1]}", "rb") as f:
                bot.send_photo(message.chat.id, f)
            return

    with open(f"./image/{random.choice(memes)}", "rb") as f:
        bot.send_photo(message.chat.id, f)
    



@bot.message_handler(commands=['start',"play"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")



@bot.message_handler(commands=['password'])
def send_pass(message):
    words = message.text.split()
    if len(words) > 1:
        password = gen_pass(int(words[1]))
    else:
        password = gen_pass(8)
    bot.reply_to(message, f"ваш пароль: {password}")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['nick'])
def send_nick(message):
    user_name = message.from_user
    bot.reply_to(message, user_name)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
