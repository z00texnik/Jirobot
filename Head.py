import logging
import time
from jira import JIRA
import telebot
from auth_data import token, url, username, password
from telebot import types

options= {
    'server': 'https://aptekarunew.atlassian.net',
    'verify': True
}
bot = telebot.TeleBot(token)
keybo = telebot.types.ReplyKeyboardMarkup(True)
au_bjra = JIRA(options=options, basic_auth=(username, password))  # переменная отвечающая за авторизацию в жиру


@bot.message_handler(
    commands=['start'])  # создаётся обработчик команды "start" и ответ на команду + возвращает имя написавшего
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton(text='Статус задачи')
    markup.add(item)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')


@bot.message_handler(commands=['help'])  # создаётся обработчик команды "help" и ответ на команду
def help(message):
    bot.send_message(message.chat.id, 'Если ты нажмёшь на /start, то ты начнёшь работу со мной.')


#@bot.message_handler(
#    content_types=['text'])  # в связке с командой issue, которая по введённому номеру возвращает статус задачи
#def handle_text(message):
#    bot.send_message(message.chat.id, 'Статус задачи: ' + au_bjra.get_issue_status(message.text))
issue_dict = {
    'project': {'key': 'ARN'},
    'summary': 'Имя задачи',
    'description': 'Описание задачи',
    'issuetype':{'name':'Баг'},
    'labels':['Внутреннее'],
    'subsystem':{'name':'Backend'}
}

def create_newIssue(issueName, descr, issueType, labels, subsystemsName):
  issue_dict = {
  'summary': issueName,
  'description': descr,
  'issuetype':{'name': issueType},
  'labels':[labels],
  'subsystem':{'name': subsystemsName}
}
  return issue_dict

#newissue= au_bjra.create_issue(fields=issue_dict)
@bot.message_handler(commands=['new_issue'])
def new_issue(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    newIssue=types.KeyboardButton('Завести задачу')
    markup.add(newIssue)
    bot.send_message(message.chat.id, 'Вводи данные по задаче по очереди: Название задачи, Описание задачи, Тип задачи, SubSystem, Лейбл(ы)')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Название задачи: ' + au_bjra(create_newIssue(issueName=message.text)) + au_bjra(create_newIssue(descr=message.text)) + au_bjra(create_newIssue(issueType=message.text)) + au_bjra(create_newIssue(subsystemsName=message.text)) + au_bjra(create_newIssue(labels=message.text))).split
#    bot.send_message(message.chat.id, 'Описание задачи: ' + au_bjra(create_newIssue(descr=message.text)))
#    bot.send_message(message.chat.id, 'Тип задачи: ' + au_bjra(create_newIssue(issueType=message.text)))
#    bot.send_message(message.chat.id, 'SubSystem: ' + au_bjra(create_newIssue(subsystemsName=message.text)))
#    bot.send_message(message.chat.id, 'Лейблы: ' + au_bjra(create_newIssue(labels=message.text)))
    return handle_text

bot.infinity_polling()  # бесконечный запуск