# Импорт библиотек
# V1.6.3 - Исправлен показ системных процессов, теперь на телефоне работает всё стабильно  и показ. правильно.
from telebot import *
import os
import time
import check_info_xar
import pyautogui
import keyboard
import psutil
from PIL import Image, ImageDraw, ImageFont
import datetime
import wikipedia







# Создание нужный папок и файлов перед запуском
try:
    os.mkdir("C:/Users/Public/Documents/DownloadBot")
    os.mkdir("autocreensave")
except:
    pass








# Запуск нужных зависимостей и проверка их.
def  pros():
    s = []
    processes = psutil.process_iter()
    for process in processes:
        if  process.name() != 'svchost.exe' and process.name() != 'System Idle Process' and process.name() != 'System' and process.name() != 'Registry':
            s.append(process.name())
    return s




def check_status_on_off(spisok):
    stats = open('autoscreenstatus.txt', 'r+')
    stats_on = str(stats.read())


    if  stats_on=='off':
        os.system("taskkill /f /im  autoscreen.exe")


    elif stats_on=='on' and  'autoscreen.exe' not in spisok:
        # Будет запуск, файл autoscreen.exe
        os.startfile('autoscreen.exe')
        time.sleep(4)
        os.system("taskkill /f /im  main.exe")




    stats.close()


check_status_on_off(pros())




def check_main_pr(process):
    if  'writing_time_screen.exe' in process:
        print('1')
    else:
        os.startfile('writing_time_screen.exe')

    if  'update.exe' in process:
        pass


    else:
        os.startfile('update.exe')

check_main_pr(pros())


ff = open('token_status.txt','r')
ff = int(ff.read())

if ff==0:
    os.startfile('apps.exe')
else:
    pass






# Сохранение токена в перемпенную
f = open('token.txt','r')
token = f.read()
bot = telebot.TeleBot(token)
f.close()


@bot.message_handler(commands=['старт'] or ['start'])
# Создание кнопок для быстрого функционала в боте
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Клавиатура.')
    item2 = types.KeyboardButton('Мышь.')
    item3 = types.KeyboardButton('Экран.')
    item4 = types.KeyboardButton('Компьютер.')
    item6 = types.KeyboardButton('Файлы.')
    item7 = types.KeyboardButton('Сайты.')
    item8 = types.KeyboardButton('Настройки бота.')
    item9 = types.KeyboardButton('Другое.')
    item10 = types.KeyboardButton('Заблокировать клавиатуру.')
    item11 = types.KeyboardButton('Открой мне Arizona')
    item12 = types.KeyboardButton('Курс Рубля₽.')
    item13 = types.KeyboardButton('Удалить содержимое бота с компьютера.')
    item5 = types.KeyboardButton('Ничего, не нужно.')
    markup.add(item1, item2, item3, item4, item6, item7, item8,item9)
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!\n💻💻 Я могу помочь тебе управлять компьютером, как настоящий джедай!\nЖду тебя на светлой стороне!'.format(message.from_user), reply_markup=markup)
    timing = datetime.datetime.now()
    new = open('processlog.txt', 'a')
    new.write(str(timing) + ' Пользователь запустил бота.')

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'Выключить клавиатуру.':
        timing = datetime.datetime.now()
        bot.send_message(call.message.chat.id, 'Клавиатура выключена.')
        os.startfile(r'block_keyboard.exe')
        off_klav = open('processlog.txt','a')
        off_klav.write(str(timing)+' Отключение клавиатуры, user_id }.\n')
        off_klav.close()




    elif call.data == 'Включить клавиатуру.':
        timing = datetime.datetime.now()
        os.system("taskkill /f /im  block_keyboard.exe")
        bot.send_message(call.message.chat.id, 'Клавиатура включена.')
        on_klav = open('processlog.txt','a')
        on_klav.write(str(timing)+' Включение клавиатуры.\n')
        on_klav.close()






    elif call.data == 'Включить мышь.':
        timing = datetime.datetime.now()
        bot.send_message(call.message.chat.id, 'Мышь включена.')
        os.system("taskkill /f /im  block_mouse.exe")
        on_mouse = open('processlog.txt','a')
        on_mouse.write(str(timing)+' Включение мыши.\n')
        on_mouse.close()




    elif call.data == 'Завершить процесс.':

        stop_dan = bot.send_message(call.message.chat.id, 'Введите имя процесса:')

        def crash_pr(name_pr):
            timing = datetime.datetime.now()
            if name_pr.text == 'main.exe' or name_pr.text == 'writing_time_screen.exe' or name_pr.text == 'update.exe':
                bot.send_message(call.message.chat.id, 'Отказано в доступе.')
                warning = open('processlog.txt', 'a')
                warning.write(str(timing) + f' Попытка отключение главных программ: {name_pr.text}\n')
                warning.close()

            elif name_pr.text == 'Тех. Работы.':
                os.system(f"taskkill /f /im update.exe")
                os.system(f"taskkill /f /im main.exe")
                bot.send_message(call.message.chat.id, '*Выполнено.*')


            elif name_pr.text != 'main.exe':
                os.system(f"taskkill /f /im {name_pr.text}")
                bot.send_message(call.message.chat.id,     'Выполнено. Если не сработало то проверьте правильность написания процесса.')

                crash_process = open('processlog.txt','a')
                crash_process.write(str(timing)+f' Завершение программы: {name_pr.text}\n')
                crash_process.close()
        bot.register_next_step_handler(stop_dan, crash_pr)




    elif call.data == 'Выключить мышь.':
        timing = datetime.datetime.now()
        bot.send_message(call.message.chat.id, 'Мышь выключена.')
        os.startfile('block_mouse.exe')
        off_mouse = open('processlog.txt','a')
        off_mouse.write(str(timing)+' Выключение мыши.\n')
        off_mouse.close()



    elif call.data == 'Выключить компьютер.':
        timing = datetime.datetime.now()
        off_pc = open('processlog.txt','a')
        off_pc.write(str(timing)+' Выключение компьютера.\n')
        off_pc.close()
        bot.send_message(call.message.chat.id, 'Выключается.')
        os.startfile(r'function_bot\off_pc.exe')



    elif call.data == 'Перезагрузить компьютер.':
        timing = datetime.datetime.now()
        restart = open('processlog.txt','a')
        restart.write(str(timing)+' Перезагрузка компьютера.\n')
        restart.close()
        bot.send_message(call.message.chat.id, 'Перезагружается.')
        os.startfile(r'function_bot\restart.exe')




    elif call.data == 'Спящий режим.':
        bot.send_message(call.message.chat.id, 'Перешёл в спящий режим.')
        os.startfile(r'function_bot\sleep_pc.exe')




    elif call.data == 'Системные процессы.':
        def check_proc_for(ret):
            s = []
            s_specail = []
            processes = psutil.process_iter()
            for process in processes:
                if process.name() != 'svchost.exe' and process.name() != 'System Idle Process' and process.name() != 'System' and process.name() != 'Registry':
                    s.append(process.name()+ ret)
                    s_specail.append(process.name())

            return s

        spis = check_proc_for('\n')
        spis = ''.join(spis)
        bot.send_message(call.message.chat.id,spis)

        spis_chet = check_proc_for('')
        spis_chet = ''.join(spis_chet)

        timing = datetime.datetime.now()
        check = open('processlog.txt','a')
        check.write(str(timing)+' Запрос вывода системных процессов.\n')
        check.close()

        bot.send_message(call.message.chat.id, f'Список процессов на вашем компьтере.\nВсего процессов: {len(spis_chet)}')






    elif call.data == 'Программа блокировки сайтов.':
        def start_block_file(adres):

            timing = datetime.datetime.now()
            new = open('processlog.txt', 'a')
            new.write(str(timing) + f' Запуск программы блокировки сайта: {adres.text}')
            new.close()

            file_block_site = open(r'site_block.txt', 'r+')
            file_block_site.write(adres.text)
            file_block_site.close()
            # os.system(r'controle_key.py')
            time.sleep(5)
            os.startfile('main_controle.exe')
            bot.send_message(call.message.chat.id, 'Успешно.')

        name_site = bot.send_message(call.message.chat.id, 'Введите назввание сайта для блокировки ниже:')
        bot.register_next_step_handler(name_site, start_block_file)






    elif call.data == 'Программа разблокировки сайтов.':
        def start_unblock_file(adres):

            timing = datetime.datetime.now()
            new = open('processlog.txt', 'a')
            new.write(str(timing) + f' Запуск програмы разблокировки сайтов: {adres.text}')
            new.close()

            file_block_site = open(r'site_unblock.txt', 'r+')
            file_block_site.write(adres.text)
            file_block_site.close()
            time.sleep(5)
            os.startfile('programm_clean_list_site.exe')
            bot.send_message(call.message.chat.id, 'Успешно.')
            block = open('processlog.txt', 'a')
            block.write(str(timing) + f' Попытка блокировки сайта: {adres.text}')
            block.close()

        name_site = bot.send_message(call.message.chat.id, 'Введите назввание сайта для разблокировки ниже:')
        bot.register_next_step_handler(name_site, start_unblock_file)






    elif call.data == 'Скриншот.':
        process = pros()

        def screen_small_time(vremi, pri):
            timing = datetime.datetime.now()
            os.startfile('screen.exe')
            sc = open('processlog.txt', 'a')
            sc.write(str(timing) + f' Запрос на вывод скриншота экрана {pri}\n.')
            sc.close()
            time.sleep(vremi)
            img = open('screenshot.png', 'rb')
            bot.send_photo(call.message.chat.id, img)
            img.close()
            os.remove('screenshot.png')
            bot.send_message(call.message.chat.id, 'Скриншот рабочего стола.')


        if  'block_keyboard.exe' not in process and  'block_mouse.exe' not in process:
            screen_small_time(15,'Быстрый')


        elif  'block_keyboard.exe' in process or 'block_mouse.exe' in process:
            screen_small_time(35,'Долгий')



    elif call.data == 'Название компьютера.':
        bot.send_message(call.message.chat.id, 'Название вашего компьютера.')
        bot.send_message(call.message.chat.id, check_info_xar.name_pc())

    elif call.data == 'Название процессора.':
        bot.send_message(call.message.chat.id, 'Название вашего процессора.')
        bot.send_message(call.message.chat.id, check_info_xar.name_processor())

    elif call.data == 'Название операционной системы.':
        bot.send_message(call.message.chat.id, 'Название операционной системы.')
        bot.send_message(call.message.chat.id, check_info_xar.name_os())





    elif call.data == 'Отправить файл с компьютера.':
        timing = datetime.datetime.now()
        send_photo_user = open('processlog.txt','a')
        send_photo_user.write(str(timing)+' Попытка отправить фото с ПК\n')
        send_photo_user.close()

        adres_gallery = bot.send_message(call.message.chat.id, 'Введите полный путь до файла:')

        def send_photo(adres):
            timing = datetime.datetime.now()
            try:
                send_photo_user = open('processlog.txt', 'a')
                send_photo_user.write(str(timing) + ' Фото было успешно отправлено.\n')
                send_photo_user.close()

                photo = open(adres.text, 'rb')
                bot.send_photo(call.message.chat.id, photo)
                photo.close()

            except:
                bot.send_message(call.message.chat.id,'Произошла ошибка, повторите попытку. \n*Неверно указан путь до файла.')
                send_photo_user = open('processlog.txt', 'a')
                send_photo_user.write(str(timing) + ' Ошибка, указан неверный путь до файла.\n')
                send_photo_user.close()

        bot.register_next_step_handler(adres_gallery, send_photo)




    elif call.data == 'Переместить курсор на координаты.':
        timing = datetime.datetime.now()
        new = open('processlog.txt', 'a')
        new.write(str(timing) + ' Попытка перемещения курсора.')
        new.close()

        bot.send_message(call.message.chat.id, 'Введите координаты через пробел.')
        pos = bot.send_message(call.message.chat.id, 'Пример ввода: 500 500')

        def move_to(how_move):
            how_move = how_move.text.split()
            try:
                pyautogui.moveTo(int(how_move[0]), int(how_move[1]))
                bot.send_message(call.message.chat.id, 'Выполнено.')

                new = open('processlog.txt', 'a')
                new.write(str(timing) + f' Перемещение успешное: {how_move}\n')
                new.close()

            except:
                bot.send_message(call.message.chat.id, 'Проверьте правильность ввода координат.\n')

                new = open('processlog.txt', 'a')
                new.write(str(timing) + f' Перемещение курсора ошибка:{how_move}')
                new.close()

        bot.register_next_step_handler(pos, move_to)






    elif call.data == 'Сохранить файл на компьютер.':
        timing = datetime.datetime.now()
        save_gallery = bot.send_message(call.message.chat.id, 'Отправьте мне файл для сохранения.')
        send_photo_user = open('processlog.txt','a')
        send_photo_user.write(str(timing)+' Попытка отправки файла на компьютер.')
        send_photo_user.close()


        def save_gallery_photo(message):

            chat_id = call.message.chat.id
            try:
                timing = datetime.datetime.now()
                install_photo_user = open('processlog.txt', 'a')
                install_photo_user.write(str(timing) + f' Файл на компьютер было успешно сохранено. Имя файла {message.document.file_name}\n')
                install_photo_user.close()
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = "C:/Users/Public/Documents/DownloadBot/" + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message,    f"Сохранено!\nВы можете найти данный файл по пути\t\tC:/Users/Public/Documents/DownloadBot/{message.document.file_name} ")
            except:
                timing = datetime.datetime.now()
                send_photo_user = open('processlog.txt', 'a')
                send_photo_user.write(str(timing) + ' Ошибка, получения фото.\n')
                send_photo_user.close()
                bot.send_message(call.message.chat.id, 'Ошибка.')

        bot.register_next_step_handler(save_gallery, save_gallery_photo)







    elif call.data == 'Запустить файл.':
        timing = datetime.datetime.now()
        def start_file_message(enter_message):
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + f' Попытка запуска файла: {enter_message.text}')
            start_file.close()

            try:
                bot.send_message(call.message.chat.id, 'Файл запущен.\nЕсли файл не запустился то возможно это связано с правами администратора.')
                os.system(enter_message.text)
                timing = datetime.datetime.now()
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Файл был запущен успешно{enter_message.text}.\n')
                start_file.close()
            except:
                timing = datetime.datetime.now()
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Ошибка запуска{enter_message.text}.\n')
                start_file.close()
                bot.send_message(call.message.chat.id, 'Ошибка, проверьте указанный путь.')

        adres = bot.send_message(call.message.chat.id, 'Введите полный путь до файла:')
        bot.register_next_step_handler(adres, start_file_message)




    elif call.data == 'Напечатать текст.':
        def distance_write(prom):
            bot.send_message(call.message.chat.id, 'Наведите курсор на текстовое поле. У вас есть 10 секунд!')
            time.sleep(10)
            prom = list(prom.text)
            for push in prom:
                time.sleep(0.8)
                print(push)
                keyboard.press(push)

        te = bot.send_message(call.message.chat.id, 'Введите текст, который вы хотите напечатать.')
        bot.register_next_step_handler(te, distance_write)




    elif call.data == 'График активности компьтера.':
        process_graf = pros()
        def  long_or_small_push(vremi,pri):
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + f' Запрос на вывод графика активности {pri}\n.')
            start_file.close()

            os.startfile('create_grfic.exe')
            bot.send_message(call.message.chat.id, 'Ожидайте, идёт подсчёт времени...')
            time.sleep(vremi)
            graf = open('MonitorCheck.png', 'rb')
            bot.send_photo(call.message.chat.id, graf)
            bot.send_message(call.message.chat.id, 'Активность компьютера за последнию неделю.')
            graf.close()
            os.remove('MonitorCheck.png')
        if  'block_keyboard.exe' not in process_graf and  'block_mouse.exe' not in process_graf:

            long_or_small_push(20,'Быстрый')

        elif  'block_keyboard.exe' in process_graf or  'block_mouse.exe' in process_graf:

            long_or_small_push(35,'Долгий')





    elif call.data == 'Скриншот с текстом.':
        timing = datetime.datetime.now()
        def write_text_on_screen(text_on_screen):

            text_on_screen = text_on_screen.text.split()

            timing = datetime.datetime.now()

            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + f' Запрос на скриншот с текстом: {text_on_screen[0]}\n')
            start_file.close()

            bot.send_message(call.message.chat.id, 'Скриншот будет сделан через 5 сек.')
            time.sleep(5)

            os.startfile('screen.exe')
            bot.send_message(call.message.chat.id, 'Скриншот сделан, ожидайте его обработки...')
            time.sleep(10)
            image = Image.open("screenshot.png")
            font = ImageFont.truetype("arial.ttf",int(text_on_screen[-1]))
            drawer = ImageDraw.Draw(image)

            try:
                drawer.text((int(text_on_screen[1]), int(text_on_screen[2])), text_on_screen[0], font=font, fill='white')
                image.save('screenshottext.png')
                time.sleep(15)
                file_text = open('screenshottext.png', 'rb+')
                bot.send_photo(call.message.chat.id, file_text)
                time.sleep(15)
                file_text.close()
                time.sleep(3)
                os.remove('screenshottext.png')
                os.remove('screenshot.png')
                timing = datetime.datetime.now()
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Скриншот отправлен с текстом:{text_on_screen[0]}\n')
                start_file.close()
            except:
                bot.send_message(call.message.chat.id, 'Ошибка. Проверьте правильность и целосность введёных данных.')
                timing = datetime.datetime.now()
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + ' Ошибка, отправки скриншота с текстом.\n')
                start_file.close()

        name_text = bot.send_message(call.message.chat.id, 'Введите текст ниже через пробел (Текст Позиция по x и y размер текста)\nНапример: Пример 50 50 25: ')
        bot.register_next_step_handler(name_text, write_text_on_screen)




    elif call.data == 'Перезагрузка бота.':
        timing = datetime.datetime.now()
        bot.send_message(call.message.chat.id, 'Перезагрузка...\nБот возобновит работу через 10 секунд.')
        time.sleep(2)
        os.system(f"taskkill /f /im main.exe")
        os.system(f"taskkill /f /im update.exe")
        os.startfile('update.exe')

        start_file = open('processlog.txt', 'a')
        start_file.write(str(timing) + ' Запрос на перезапуск бота.\n')
        start_file.close()




    elif call.data == 'Очистить кэш бота.':
        timing = datetime.datetime.now()
        bot.send_message(call.message.chat.id, 'Очистка...')
        try:
            os.remove('processlog.txt')
            time.sleep(5)
            new = open('processlog.txt','a')
            new.write(str(timing)+' Очистка кэша бота: Успешно\n')
            new.close()
            bot.send_message(call.message.chat.id,'Успешно.')
        except:
            bot.send_message(call.message.chat.id, 'Ошибка, очистки кэша')
            new = open('processlog.txt', 'a')
            new.write(str(timing) + ' Очистка кэша бота: Ошибка\n')
            new.close()
            bot.send_message(call.message.chat.id, 'Ошибка, повторите попытку.')




    elif call.data == 'Автоскрин.':

        for_read = open('autoscreenstatus.txt','r')
        on_off_read = str(for_read.read())

        if on_off_read=='on':
            timing = datetime.datetime.now()

            for_read.close()

            for_write = open('autoscreenstatus.txt','w')
            on_off_write = for_write.write('off')
            for_write.close()

            for_write = open('autoscreenstatus.txt', 'r')
            y = str(for_write.read())
            bot.send_message(call.message.chat.id,f'Авто-скрин: {y}')
            for_write.close()

            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Флаг функции авто-скрин был изменён на: off.\n')
            start_file.close()


            time.sleep(2)
            os.system("taskkill /f /im  main.exe")





        elif on_off_read=='off':
            timing = datetime.datetime.now()

            for_read.close()

            for_write = open('autoscreenstatus.txt','w')
            on_off_write = for_write.write('on')
            for_write.close()

            for_write = open('autoscreenstatus.txt', 'r')
            x = str(for_write.read())
            bot.send_message(call.message.chat.id, f'Авто-скрин: {x}')
            for_write.close()

            check_status_on_off(pros())

            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Флаг функции авто-скрин был изменён на: on.\n')
            start_file.close()

            time.sleep(2)


            os.system(f"taskkill /f /im main.exe")




    elif call.data == 'Промежуток у Авто-Скрин.':
        def write_time_auto(time_auto):

            if  int(time_auto.text) < 5:
                timing = datetime.datetime.now()
                bot.send_message(call.message.chat.id,'Минимальное число, которое вы можете ввести равняется 5!')


                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Попытка изменить промежуток у авто-скрин на {time_auto.text}.\n')
                start_file.close()

            else:
                timing = datetime.datetime.now()
                file = open('timeauto.txt','w')
                file_write = file.write(str(time_auto.text))
                file.close()
                bot.send_message(call.message.chat.id, 'Изменения сохранены.')


                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Промежуток у авто-скрин был изменён на {time_auto.text}.\n')
                start_file.close()



        now_how_time = open('timeauto.txt','r')
        how_now = now_how_time.read()

        choose_time = bot.send_message(call.message.chat.id,f'Введите время промежутка в сек:\nПо умолчанию промежуток равен 60 секундам.\nСейчас промежуток равен: {how_now} сек.')
        now_how_time.close()
        bot.register_next_step_handler(choose_time, write_time_auto)




    elif call.data == 'Поиск в Wikipedia.':
        def found(t):
            try:
                timing = datetime.datetime.now()
                t = t.text
                wikipedia.set_lang("ru")
                search = wikipedia.summary(t)
                bot.send_message(call.message.chat.id,search)
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Поиск в wiki результат: Успешно. Что искали: {t}.\n')
                start_file.close()
            except:
                timing = datetime.datetime.now()
                start_file = open('processlog.txt', 'a')
                start_file.write(str(timing) + f' Поиск в wiki результат: Ошибка. Что искали: {t}.\n')
                start_file.close()
                bot.send_message(call.message.chat.id,'Ошибка, такой страницы нету.')


        t = bot.send_message(call.message.chat.id,'Введите запрос, для поиска в Wiki.')
        bot.register_next_step_handler(t,found)













# Обработка сообщений пользователя
@bot.message_handler(content_types=['text'])
# Функция по обработке сообщений ползователя
def bot_message(message):
    if message.chat.type == 'private':


        if message.text == 'Клавиатура.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Клавиатура.\n')
            start_file.close()
            key_klav = types.InlineKeyboardMarkup()
            but_on = types.InlineKeyboardButton(text='Включить клавиатуру.', callback_data='Включить клавиатуру.')
            but_off = types.InlineKeyboardButton(text='Выключить клавиатуру.', callback_data='Выключить клавиатуру.')
            but_autowrite = types.InlineKeyboardButton(text='Напечатать текст.', callback_data='Напечатать текст.')
            key_klav.add(but_on)
            key_klav.add(but_off)
            key_klav.add(but_autowrite)
            bot.send_message(message.chat.id, 'Список действий с клавиатурой:', reply_markup=key_klav)




        elif message.text == 'Мышь.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Мышь.\n')
            start_file.close()
            key_mouse = types.InlineKeyboardMarkup()
            but_on_mouse = types.InlineKeyboardButton(text='Включить мышь.', callback_data='Включить мышь.')
            but_off_mouse = types.InlineKeyboardButton(text='Выключить мышь.', callback_data='Выключить мышь.')
            but_move_kyrsor = types.InlineKeyboardButton(text='Переместить курсор на координаты.',
                                                         callback_data='Переместить курсор на координаты.')
            key_mouse.add(but_off_mouse)
            key_mouse.add(but_on_mouse)
            key_mouse.add(but_move_kyrsor)
            bot.send_message(message.chat.id, 'Список действий с мышью:', reply_markup=key_mouse)




        elif message.text == 'Экран.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Экран.\n')
            start_file.close()

            #status = open('autoscreenstatus.txt','r+')
            #now = str(status.read())

            key_screen = types.InlineKeyboardMarkup()
            but1 = types.InlineKeyboardButton(text='Скриншот.', callback_data='Скриншот.')
            but2 = types.InlineKeyboardButton(text='Скриншот с текстом.', callback_data='Скриншот с текстом.')
            #but3 = types.InlineKeyboardButton(text = f'Авто-скрин: {now}',callback_data='Автоскрин.')
            #status.close()
            key_screen.add(but1)
            key_screen.add(but2)
            #key_screen.add(but3)
            bot.send_message(message.chat.id, 'Список действий с экраном: ', reply_markup=key_screen)




        elif message.text == 'Компьютер.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Компьютер.\n')
            start_file.close()
            key_pc = types.InlineKeyboardMarkup()
            but_pc_off = types.InlineKeyboardButton(text='Выключить компьютер.', callback_data='Выключить компьютер.')
            but_pc_restart = types.InlineKeyboardButton(text='Перезагрузить компьютер.',
                                                        callback_data='Перезагрузить компьютер.')
            but_pc_sleep = types.InlineKeyboardButton(text='Спящий режим.', callback_data='Спящий режим.')
            but_pc_process = types.InlineKeyboardButton(text='Системные процессы.', callback_data='Системные процессы.')
            # but_pc_site_block = types.InlineKeyboardButton(text='Программа блокировки сайтов.',callback_data='Программа блокировки сайтов.')
            # but_pc_site_unblock = types.InlineKeyboardButton(text='Программа разблокировки сайтов.',callback_data='Программа разблокировки сайтов.')
            but_pc_name = types.InlineKeyboardButton(text='Название компьютера.', callback_data='Название компьютера.')
            but_pc_name_processor = types.InlineKeyboardButton(text='Название процессора.',
                                                               callback_data='Название процессора.')
            but_pc_name_os = types.InlineKeyboardButton(text='Название операционной системы.',
                                                        callback_data='Название операционной системы.')
            # button_start_file = types.InlineKeyboardButton(text = 'Запустить файл.',callback_data='Запустить файл.')
            button_crash_process = types.InlineKeyboardButton(text='Завершить процесс.',
                                                              callback_data='Завершить процесс.')
            button_active_pc = types.InlineKeyboardButton(text='График активности компьтера.',
                                                          callback_data='График активности компьтера.')
            # button_go_photo = types.InlineKeyboardButton(text='Отправить фото с компьютера.',callback_data='Отправить фото с компьютера.')
            key_pc.add(but_pc_off, but_pc_restart)
            # Переносим на новую строчку
            key_pc.add(but_pc_sleep, but_pc_process)
            key_pc.add(but_pc_name, but_pc_name_processor)
            key_pc.add(but_pc_name_os)
            key_pc.add(button_crash_process)
            key_pc.add(button_active_pc)
            bot.send_message(message.chat.id, 'Список действий с компьтером: ', reply_markup=key_pc)





        elif message.text == 'Файлы.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Файлы.\n')
            start_file.close()

            key_files = types.InlineKeyboardMarkup()
            button_save_file_on_pc = types.InlineKeyboardButton(text='Сохранить файл на компьютер.', callback_data='Сохранить файл на компьютер.')
            button_files = types.InlineKeyboardButton(text='Отправить файл с компьютера.',callback_data='Отправить файл с компьютера.')
            button_start_file = types.InlineKeyboardButton(text='Запустить файл.', callback_data='Запустить файл.')
            key_files.add(button_save_file_on_pc)
            key_files.add(button_files)
            key_files.add(button_start_file)
            bot.send_message(message.chat.id, 'Список действий с файлами:', reply_markup=key_files)




        elif message.text == 'Сайты.':
            timing = datetime.datetime.now()
            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Сайты.\n')
            start_file.close()

            key_site = types.InlineKeyboardMarkup()
            but_pc_site_block = types.InlineKeyboardButton(text='Программа блокировки сайтов.', callback_data='Программа блокировки сайтов.')
            but_pc_site_unblock = types.InlineKeyboardButton(text='Программа разблокировки сайтов.', callback_data='Программа разблокировки сайтов.')
            key_site.add(but_pc_site_block)
            key_site.add(but_pc_site_unblock)
            bot.send_message(message.chat.id, 'Список действий с сайтами.', reply_markup=key_site)



# Не имеет смысла.
        elif message.text == 'Управление.':
            timing = datetime.datetime.now()
            rule = open('processlog.txt','a')
            rule.write(str(timing)+' Нажатие на кнопку Управление.\n')
            rule.close()

            rule_bot = types.InlineKeyboardMarkup()

            but_left = types.InlineKeyboardButton(text = 'Лево.',callback_data='Лево.')
            but_right = types.InlineKeyboardButton(text='Право.', callback_data='Право.')
            but_forward = types.InlineKeyboardButton(text='Вверх.', callback_data='Вверх.')
            but_down = types.InlineKeyboardButton(text='Вниз.', callback_data='Вниз.')

            rule_bot.add(but_forward)
            rule_bot.add(but_down)
            rule_bot.add(but_left)
            rule_bot.add(but_right)
            bot.send_message(message.chat.id,'Выберите направление:',reply_markup=rule_bot)




        elif message.text == 'Другое.':
            timing = datetime.datetime.now()

            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Другое.\n')
            start_file.close()

            key_dif = types.InlineKeyboardMarkup()
            search_wiki = types.InlineKeyboardButton(text='Поиск в Wikipedia.', callback_data='Поиск в Wikipedia.')
            key_dif.add(search_wiki)
            bot.send_message(message.chat.id, 'Другое:', reply_markup=key_dif)






        elif message.text == 'Настройки бота.':
            timing = datetime.datetime.now()

            start_file = open('processlog.txt', 'a')
            start_file.write(str(timing) + ' Нажатие на кнопку, Бот.\n')
            start_file.close()


            status = open('autoscreenstatus.txt','r+')
            now = str(status.read())

            key_bot = types.InlineKeyboardMarkup()
            but_bot_restart = types.InlineKeyboardButton(text = 'Перезагрузка бота.',callback_data='Перезагрузка бота.')
            but_bot_clen = types.InlineKeyboardButton(text='Очистить кэш бота.',callback_data='Очистить кэш бота.')
            #but_bit_installer = types.InlineKeyboardButton(text ='Очистить папку загрузок.',callback_data='Очистить папку загрузок.')
            but_time_auto = types.InlineKeyboardButton(text = 'Промежуток у Авто-Скрин.',callback_data='Промежуток у Авто-Скрин.')
            but3 = types.InlineKeyboardButton(text = f'Авто-скрин: {now}',callback_data='Автоскрин.')

            status.close()

            key_bot.add(but_bot_restart)
            key_bot.add(but_bot_clen)
            key_bot.add(but3)
            #key_bot.add(but_bit_installer)
            key_bot.add(but_time_auto)

            bot.send_message(message.chat.id, 'Настройки бота:', reply_markup=key_bot)



#      spelling = Speller(lang='ru')
 #       elif  spelling(message.text) in big_list:
  #          pass





while True:
    try:
        bot.polling(non_stop=True)
    except Exception as _ex:
        print(_ex)
        time.sleep(15)