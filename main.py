# Импорт библиотек
from telebot import *
import os
import time
import check_info_xar
import pyautogui





# Сохранение токена в перемпенную
bot = telebot.TeleBot('6445792868:AAF2UZH9RdZvgvdaRFdGkPPFy7sqORd_5UU')
bot.set_webhook()


@bot.message_handler(commands=['start'])
# Создание кнопок для быстрого функционала в боте
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Клавиатура.')
    item2 = types.KeyboardButton('Мышь.')
    item3 = types.KeyboardButton('Экран.')
    item4 = types.KeyboardButton('Компьютер.')
    item6 = types.KeyboardButton('Показать список процессов на ПК!')
    item7 = types.KeyboardButton('Перезагрузить компьютер.')
    item8 = types.KeyboardButton('Ввести ПК в спящий режим!')
    item9 = types.KeyboardButton('Заблокировать мышь.')
    item10 = types.KeyboardButton('Заблокировать клавиатуру.')
    item11 = types.KeyboardButton('Открой мне Arizona')
    item12 = types.KeyboardButton('Курс Рубля₽.')
    item13 = types.KeyboardButton('Удалить содержимое бота с компьютера.')
    item5 = types.KeyboardButton('Ничего, не нужно.')
    markup.add(item1,item2,item3,item4)
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == 'Выключить клавиатуру.':
        bot.send_message(call.message.chat.id,'Клавиатура выключена.')
        os.startfile(r'block_keyboard.exe')

    elif call.data == 'Включить клавиатуру.':
        try:
            os.system("taskkill /f /im  block_keyboard.exe")
            bot.send_message(call.message.chat.id, 'Клавиатура включена.')
        except:
            bot.send_message(call.message.chat.id,'Возникла ошибка при включении клавиатуры! Повторите попытку.')





    elif call.data == 'Включить мышь.':
        bot.send_message(call.message.chat.id,'Мышь включена.')
        try:
            os.system("taskkill /f /im  block_mouse.exe")
        except:
            bot.send_message(call.message.chat.id, 'Возникла ошибка во время выключения мыши! Повторите попытку.')



    elif call.data == 'Завершить процесс.':
        stop_dan = bot.send_message(call.message.chat.id,'Введите имя процесса:')
        def crash_pr(name_pr):
            os.system(f"taskkill /f /im {name_pr.text}")
            bot.send_message(call.message.chat.id,'Выполнено. Если не сработало то проверьте правильность написания процесса.')
        bot.register_next_step_handler(stop_dan,crash_pr)


    elif call.data == 'Выключить мышь.':
        bot.send_message(call.message.chat.id,'Мышь выключена.')
        os.startfile(r'block_mouse.exe')

    elif call.data == 'Выключить компьютер.':
        bot.send_message(call.message.chat.id,'Выключен.')
        os.startfile(r'function_bot\off_pc.py')

    elif call.data == 'Перезагрузить компьютер.':
        bot.send_message(call.message.chat.id,'Перезагружен.')
        os.startfile(r'function_bot\restart.py')

    elif call.data == 'Спящий режим.':
        bot.send_message(call.message.chat.id,'В спящем режиме.')
        os.startfile(r'function_bot\sleep_pc.py')

    elif call.data == 'Системные процессы.':
        os.startfile(r'function_bot\process.py')
        process = open('process.txt','r+')
        process_enter = process.read()
        bot.send_message(call.message.chat.id,process_enter)
        bot.send_message(call.message.chat.id,'Список процессов на вашем компьтере.')

    elif call.data == 'Программа блокировки сайтов.':
        bot.send_message(call.message.chat.id, 'Введите сайты на компьютеры.')
        os.system(r'controlebrow\main_controle.exe')


    elif call.data == 'Программа разблокировки сайтов.':
        bot.send_message(call.message.chat.id, 'Введите сайты на компьтере.')
        os.system(r'controlebrow\programm_clean_list_site.exe')


    elif call.data == 'Скриншот.':
        os.startfile(r'function_bot\screen.exe')
        # Три секунды нормальная обработка меньше не надо, будут ошибки
        time.sleep(5)
        img = open(r'screenshot.png','rb')
        bot.send_photo(call.message.chat.id,img)
        img.close()
        os.remove('screenshot.png')
        bot.send_message(call.message.chat.id,'Скриншот рабочего стола.')

    elif call.data == 'Название компьютера.':
        bot.send_message(call.message.chat.id, 'Название вашего компьютера.')
        bot.send_message(call.message.chat.id,check_info_xar.name_pc())

    elif call.data == 'Название процессора.':
        bot.send_message(call.message.chat.id, 'Название вашего процессора.')
        bot.send_message(call.message.chat.id, check_info_xar.name_processor())

    elif call.data == 'Название операционной системы.':
        bot.send_message(call.message.chat.id, 'Название операционной системы.')
        bot.send_message(call.message.chat.id,check_info_xar.name_os())

    elif call.data == 'Переместить курсор на координаты.':
        bot.send_message(call.message.chat.id,'Введите координаты через пробел.')
        pos = bot.send_message(call.message.chat.id, 'Пример ввода: 500 500')
        def move_to(xy):
            xy = xy.text.split()
            try:
                pyautogui.moveTo(int(xy[0]),int(xy[1]))
                bot.send_message(call.message.chat.id, 'Выполнено.')

            except:
                bot.send_message(call.message.chat.id, 'Проверьте правильность ввода координат.')
        bot.register_next_step_handler(pos, move_to)


    elif call.data == 'Сохранить фото на компьтер.':
        save_gallery = bot.send_message(call.message.chat.id,'Отправьте мне фото для сохранения.')
        def save_gallery_photo(save_photo):
            save_photo = str(save_photo.text)
            save = open('1'+save_photo+'.png','w')
            save.close()
        bot.register_next_step_handler(save_gallery, save_gallery_photo)
        











    elif call.data == 'Запустить файл.':
        def start_file_message(enter_message):
            a = 'Ошибка.'
            b = 'Верно.'
            try:
                bot.send_message(call.message.chat.id,   'Файл запущен.\nЕсли файл не запустился то возможно это связано с правами администратора.')
                os.system(enter_message.text)
            except:
                bot.send_message(call.message.chat.id, 'Ошибка, проверьте указанный путь.')
        adres = bot.send_message(call.message.chat.id,'Введите полный путь до файла:')
        bot.register_next_step_handler(adres, start_file_message)








# Обработка сообщений пользователя
@bot.message_handler(content_types=['text'])
# Функция по обработке сообщений ползователя
def bot_message(message):
    if message.chat.type == 'private':


        if message.text == 'Клавиатура.':
            key_klav = types.InlineKeyboardMarkup()
            but_on = types.InlineKeyboardButton(text = 'Включить клавиатуру.',callback_data='Включить клавиатуру.')
            but_off = types.InlineKeyboardButton(text='Выключить клавиатуру.',callback_data='Выключить клавиатуру.')
            key_klav.add(but_on,but_off)
            bot.send_message(message.chat.id, 'Выбор действий с клавиатурой:', reply_markup=key_klav)


        elif message.text == 'Мышь.':
            key_mouse = types.InlineKeyboardMarkup()
            but_on_mouse = types.InlineKeyboardButton(text = 'Включить мышь.',callback_data='Включить мышь.')
            but_off_mouse = types.InlineKeyboardButton(text='Выключить мышь.', callback_data='Выключить мышь.')
            but_move_kyrsor = types.InlineKeyboardButton(text = 'Переместить курсор на координаты.',callback_data='Переместить курсор на координаты.')
            key_mouse.add(but_on_mouse,but_off_mouse)
            key_mouse.add(but_move_kyrsor)
            bot.send_message(message.chat.id, 'Выбор действий с мышью:', reply_markup=key_mouse)

        elif message.text == 'Экран.':
            key_screen = types.InlineKeyboardMarkup()
            but1  = types.InlineKeyboardButton(text = 'Скриншот.',callback_data='Скриншот.')
            but2 = types.InlineKeyboardButton(text = 'Неизвестно',callback_data='Неизвестно')
            key_screen.add(but1,but2)
            bot.send_message(message.chat.id,'Выбор действий с экраном: ',reply_markup=key_screen)

        elif message.text == 'Компьютер.':
            key_pc = types.InlineKeyboardMarkup()
            but_pc_off = types.InlineKeyboardButton(text = 'Выключить компьютер.',callback_data='Выключить компьютер.')
            but_pc_restart = types.InlineKeyboardButton(text = 'Перезагрузить компьютер.',callback_data='Перезагрузить компьютер.')
            but_pc_sleep = types.InlineKeyboardButton(text = 'Спящий режим.',callback_data='Спящий режим.')
            but_pc_process = types.InlineKeyboardButton(text = 'Системные процессы.',callback_data='Системные процессы.')
            but_pc_site_block = types.InlineKeyboardButton(text='Программа блокировки сайтов.',callback_data='Программа блокировки сайтов.')
            but_pc_site_unblock = types.InlineKeyboardButton(text='Программа разблокировки сайтов.',callback_data='Программа разблокировки сайтов.')
            but_pc_name = types.InlineKeyboardButton(text='Название компьютера.',callback_data='Название компьютера.')
            but_pc_name_processor = types.InlineKeyboardButton(text = 'Название процессора.',callback_data='Название процессора.')
            but_pc_name_os = types.InlineKeyboardButton(text='Название операционной системы.',callback_data='Название операционной системы.')
            button_start_file = types.InlineKeyboardButton(text = 'Запустить файл.',callback_data='Запустить файл.')
            button_crash = types.InlineKeyboardButton(text ='Завершить процесс.',callback_data='Завершить процесс.')
            button_save = types.InlineKeyboardButton(text='Сохранить фото на компьтер.',callback_data='Сохранить фото на компьтер.')


            key_pc.add(but_pc_off,but_pc_restart)
            # Переносим на новую строчку
            key_pc.add(but_pc_sleep,but_pc_process)
            key_pc.add(but_pc_site_block)
            key_pc.add(but_pc_site_unblock)
            key_pc.add(but_pc_name,but_pc_name_processor)
            key_pc.add(but_pc_name_os,button_start_file)
            key_pc.add(button_crash,button_save)

            bot.send_message(message.chat.id,'Выбор действий с компьтером: ',reply_markup=key_pc)

        elif message.text == 'Wi-Fi':
            key_wifi = types.InlineKeyboardMarkup()
            but_pc_off_wifi = types.InlineKeyboardButton(text = 'Выключить Wi-Fi.',callback_data='Выключить Wi-Fi.')
            key_wifi.add(but_pc_off_wifi)
            bot.send_message(message.chat.id,'Выбор действий с Wi-Fi:')





bot.polling(non_stop=True)