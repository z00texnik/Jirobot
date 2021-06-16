from atlassian import Jira
import telebot
from telebot import types



bot = telebot.TeleBot('1616090561:AAHO6hhu4sE0jhVuCPb0fD1Rt_FURZYgZSk')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
bot1 = Jira(
    url='https://aptekarunew.atlassian.net/',
    username='katren.apteka.ru.jira@gmail.com',
    password="dJ57bvyQDzEaO6GCZTYk4C0E",
    cloud=True)
JQL = 'project = ARN AND status = Done AND fixVersion = null' # это переменная JQL запроса


@bot.message_handler(commands=['start']) # реагирует на команду Старт
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет! Я ЖироБот. Я буду тебе помогать в работе, {message.from_user.first_name}')

@bot.message_handler(commands=['issue']) # попытка по команде issue получить статус задачи
def issue_key_status(message):
    bot.send_message(message.chat.id, f'Введи номер задачи:')
    if message.text.lower() == bot1.issue(key=input()): #вот тут у меня по задумке должен быть ввод ключа задачи
        bot.send_message(message.chat.id, 'Статус: ', bot1.get_issue_status())
    else:
        bot.send_message(message.chat.id, 'Задача не найдена')


@bot.message_handler(commands=['jql']) # попытка получить список задач за месяц
def done_issues(message):
    bot.send_message(message.chat.id, bot1.csv(jql=JQL, all_fields=all))


@bot.message_handler(content_types=['text'])  # общение с ботом, три реакции
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id,
                             f'Шалом, {message.from_user.first_name}!')
    elif message.text.lower() == 'ты не оч':
        bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEBGvFgZyRsfYgsX6eTJHuvylNoT1i6PQACGQEAAp38IwABOg9S5nIChhoeBA')
    # else:
    #     bot.send_message(message.from_user.id,
    #                       f'{message.from_user.first_name}, Я ещё учусь и тебя пока не понимаю.')



@bot.message_handler(content_types=['sticker'])
def sticker_id(messages):
    print(messages)


@bot.message_handler(content_types=['sticker'])
def print(message):
    bot.send_message(message.chat.id, 'Ну ты глупый что ли совсем?')


@bot.message_handler(commands=['help'])
def help(message):
    print(message.chat)



bot.polling(none_stop=True)
