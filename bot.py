# from typing import Any
# from webbrowser import get
from cgitb import text
from atlassian import Jira
from jira import JIRA
import telebot
from auth_data import token, url, username, password
from telebot import types

bot = telebot.TeleBot(token)
keybo = telebot.types.ReplyKeyboardMarkup(True)
au_bjra = Jira(url, username, password, cloud=True) #переменная отвечающая за авторизацию в жиру





@bot.message_handler(commands=['start']) #создаётся обработчик команды "start" и ответ на команду
def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton(text='Статус задачи')
    markup.add(item)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

@bot.message_handler(commands=['help']) #создаётся обработчик команды "help" и ответ на команду
def help(message):
    bot.send_message(message.chat.id, 'Если ты нажмёшь на /start, то ты начнёшь работу со мной. Так же ты можешь через меня посмотреть статус задачи,\
 создать задачу, оставить комментарий. Так же ты можешь выбрать команду /issue, ввести номер задачи и получишь её статус')

# @bot.message_handler(content_types=['text'])  # общение с ботом, три реакции
# def get_text_messages(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.from_user.id,
#                              f'Шалом, {message.from_user.first_name}!')
#     elif message.text.lower() == 'ты не оч':
#         bot.send_sticker(message.chat.id,
#                              'CAACAgIAAxkBAAEBGvFgZyRsfYgsX6eTJHuvylNoT1i6PQACGQEAAp38IwABOg9S5nIChhoeBA')
#     elif message.text.lower() == 'ты не очень':
#         bot.send_sticker(message.chat.id,
#                              'CAACAgIAAxkBAAEBGvFgZyRsfYgsX6eTJHuvylNoT1i6PQACGQEAAp38IwABOg9S5nIChhoeBA')
    

@bot.message_handler(commands=['issue'])
def issue(message):
    bot.send_message(message.chat.id, 'Введи номер:')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Статус задачи: ' + au_bjra.get_issue_status(f"ARN-{message.text}"))
    


bot.infinity_polling()
