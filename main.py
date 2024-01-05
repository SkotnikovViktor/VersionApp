# Импорт библиотек
from telebot import *
import os
import time



# Сохранение токена в перемпенную
bot = telebot.TeleBot('6445792868:AAF2UZH9RdZvgvdaRFdGkPPFy7sqORd_5UU')


@bot.message_handler(commands=['start'])
# Создание кнопок для быстрого функционала в боте
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Выключить ПК!')
    item2 = types.KeyboardButton('Скриншот экрана!')
    item3 = types.KeyboardButton('Запустить КонтрольБраузера для добавления сайта.')
    item4 = types.KeyboardButton('Запустить КонтрольБраузера для удаления сайта.')
    item6 = types.KeyboardButton('Показать список процессов на ПК!')
    item7 = types.KeyboardButton('Перезагрузить ПК!')
    item8 = types.KeyboardButton('Ввести ПК в спящий режим!')
    item9 = types.KeyboardButton('Курс Доллара$.')
    item10 = types.KeyboardButton('Курс Евро€.')
    item11 = types.KeyboardButton('Открой мне Arizona')
    item12 = types.KeyboardButton('Курс Рубля₽.')
    item13 = types.KeyboardButton('Скриншот экрана.')
    item5 = types.KeyboardButton('Ничего, не нужно.')
    markup.add(item1, item2, item3, item4, item11, item6, item7, item8, item9, item10, item12, item5, item13)
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!'.format(message.from_user), reply_markup=markup)


# Обработка сообщений пользователя
@bot.message_handler(content_types=['text'])
# Функция по обработке сообщений ползователя
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Выключить ПК!':
            os.startfile(r'function_bot\off_pc.py')
            time.sleep(50)
            bot.send_message(message.chat.id,'Выключено!')
        elif message.text == 'Скриншот экрана!':
            os.startfile(r'function_bot\screen.exe')
            time.sleep(5)
            img = open('screenshot.png','rb')
            bot.send_photo(message.chat.id,img)
            img.close()
            os.remove('screenshot.png')
            bot.send_message(message.chat.id,'Скриншот рабочего стола.')
        elif message.text == 'Показать список процессов на ПК!':
            os.startfile(r'function_bot\process.py')
            process = open(r'function_bot\process.txt','r+')
            process_enter = process.read()
            bot.send_message(message.chat.id,process_enter)
            process.close()
        elif message.text == 'Запустить КонтрольБраузера для добавления сайта.':
            os.startfile(r'controlebrow\main_controle.py')
bot.polling(non_stop=True)