import logging
import time
from jira import JIRA
import telebot
from auth_data import token, username, password
from telebot import types

options= {
    'server': 'https://aptekarunew.atlassian.net',
    'verify': True
}
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start=types.KeyboardButton('start')
au_bjra = JIRA(options=options, basic_auth=(username, password))  # переменная отвечающая за авторизацию в жиру


@bot.message_handler(commands=['start'])  # создаётся обработчик команды "start" и ответ на команду + возвращает имя написавшего
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton('Создать задачу')
    markup.add(start)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)


@bot.message_handler(commands=['help'])  # создаётся обработчик команды "help" и ответ на команду
def help(message):
    bot.send_message(message.chat.id, 'Если ты нажмёшь на /start, то ты начнёшь работу со мной.')


#@bot.message_handler(
#    content_types=['text'])  # в связке с командой issue, которая по введённому номеру возвращает статус задачи
#def handle_text(message):
#    bot.send_message(message.chat.id, 'Статус задачи: ' + au_bjra.get_issue_status(message.text))

def create_newIssue(projectKey, issueName, descr, issueType, labels):
  issue_dict = {
  'project':{'key': projectKey},
  'summary': issueName,
  'description': descr,
  'issuetype':{'name': issueType},
  'labels':[labels],
}
  return issue_dict



#newissue= au_bjra.create_issue(fields=issue_dict)
@bot.message_handler(content_types=['text'])
def new_issue(message):
    if message.text == 'Создать задачу':
        bot.send_message(message.chat.id, 'Вводи данные по задаче по очереди: Название проекта, Название задачи, Описание задачи, Тип задачи, Лейбл(ы)')
        issue_fuck = message.text
        issue_fuck = issue_fuck.split('\n')
    b = create_newIssue(issue_fuck[0], issue_fuck[1], issue_fuck[2], issue_fuck[3], issue_fuck[4])
    au_bjra.create_issue(fields=b)
    bot.send_message(message.chat.id, 'Задача заведена')


#@bot.message_handler(content_types=['text'])
#def handle_text(message):
#    issue_fuck=message.text
#    issue_fuck=issue_fuck.split('\n')
#    b=create_newIssue(issue_fuck[0], issue_fuck[1], issue_fuck[2], issue_fuck[3], issue_fuck[4])
#    au_bjra.create_issue(fields=b)


bot.infinity_polling()  # бесконечный запуск
