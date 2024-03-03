## Импорт библиотек для работы самого кода
## Импорт tkinter для создание интерфейса приложения
#from tkinter import *
## Импорт библиотеки для загрузки файлов
#
## Создание переменных
#check_watch_button = 0
#
## Создание окна:
## Создаём переменную windows и присваиваем ей метод по созданию окна Tk()
#windows = Tk()
## Стави флашки на запрет, измменения геометри окна
#windows.resizable(width=False,height=False)
## Указываем размеры окна по x и y
#windows.geometry('680x500')
## Даём название нашему окну и всему главному приложению
#windows.title('Настройки')
#
#
##### Начало функции по установке версии файла
#def install_file():
#       global out_infomation_install
#       # Собираем информации из виджета entry
#       information_choose_op = input_name_op.get()
#       # Убираем лишние пробелы в ведёном название операционной системы
#       information_choose_op = information_choose_op.replace(' ','')
#       # Создаём список с навзанием опреационных систем по типу windows
#       choose_windows_system = ['Windows10','windows10','Windows7','windows7','Windows8','windows8']
#       # Создаём список с навзанием опреационных систем по типу linux
#       choose_linux_system= ['LinuxMint','linuxmint','linux','Linux','LinuxUbuntu','linuxubuntu']
#
#        # Проверяем есть в ведёной строчке операционная с названием linux и так далее
#       if information_choose_op in choose_linux_system:
#            # Вывод текста об установке, программы для linux систем
#            out_information_install = Label(text=f'Начинаю установку программы для операционной системы: {information_choose_op}',font='Ubuntu',fg='green');out_information_install.place(x=1,y=250)
#            #wget.download('https://drive.google.com/file/d/1VeukkuOYLjaci5JRMca64TRxfClrllxS/view?usp=sharing')
#        # Проверка есть ли совпадания в списке и введёных данных от пользователя
#       elif information_choose_op in choose_windows_system:
#            # Выводим текст об установке программы для windows систем
#            out_information_install = Label(text=f'Начинаю установку программы для операционной системы: {information_choose_op}',font='Ubuntu',fg='green');out_information_install.place(x=1,y=250)
#            #wget.download('https://drive.google.com/file/d/1VeukkuOYLjaci5JRMca64TRxfClrllxS/view?usp=sharing')
#
#        # Исключение если пользователь ввёл не то, что нужно или неправильно написал название ОП
#       else:
#           out_infomation_false = Label(text='Такой системы нет! Проверьте написание!',font='Ubuntu',fg='red',underline=0);out_infomation_false.place(x=1,y=250)
##### Конец функции
#
#
#
#
## Здесь создаётся функция по сохранению информации об операционной системы пользователя
#### Начало функции
#def save_op():
#    # Объявляем глобальную переменную name_op
#    global name_op,check_watch_button
#    # Создана переменная name_op для того, чтобы принять информацию об введёном ОП пользователя
#    name_op = input_name_op.get()
#    if len(name_op)==0:
#           label_save= Label(text='Введите название ОП!',fg = 'red',underline=0);label_save.place(x=340,y=62)
#    else:
#        if check_watch_button==1:
#                label_save= Label(text='Изменения сохранены!',fg = 'green',underline=0);label_save.place(x=340,y=62)
#                # Создаём кнопку для установки программы для введёной ОП, а также проверяем отступ
#                button_install_program = Button(text=f'Установить программу для: {name_op}',underline=0,command=install_file);button_install_program.place(x=400-len(name_op)*3,y=465)
#                # Сохраняем эту информацию в файл с флагом "w" если файл нету, то создаётся новый, а если есть то файл перезаписываеться
#                file_op = open('information_op.txt','w')
#                # Записываем эту информацию в файл, и убираем все пробелы методом replace
#                file_op.write(name_op.replace(' ',''))
#        else:
#            label_save = Label(text='Сохранено!',fg='green',underline=0);label_save.place(x=390,y=64)
#            # Создаём кнопку для установки программы для введёной ОП, а также проверяем отступ
#            button_install_program = Button(text=f'Установить программу для: {name_op}',underline=0,command=install_file);button_install_program.place(x=400-len(name_op)*3,y=465)
#            # Сохраняем эту информацию в файл с флагом "w" если файл нету, то создаётся новый, а если есть то файл перезаписываеться
#            file_op = open('information_op.txt','w')
#            # Записываем эту информацию в файл, и убираем все пробелы методом replace
#            file_op.write(name_op.replace(' ',''))
#    check_watch_button = 1
#    return name_op
#    #### Конец функции
#
#
#
#
## Создаём текстовое поле, с текстом "Напишите полное название вашей ОП"
#text_PO = Label(text='Напишите полное название вашей операционной системы:',font='Ubuntu',underline=0);text_PO.place(x=1,y=0)
## Создаём текстовое поле, с примеро ввода текста
#text_PO_primer = Label(text='Например: Linux, Windows 7-11.',font='Ubuntu',underline=10);text_PO_primer.place(x=1,y=35)
## Создаем поле для ввода текста с название ОП
#input_name_op = Entry(text = 'Введите название ПО:',font='Ubuntu',foreground='black',width=35);input_name_op.place(x=1,y=60)
## Создаем кнопку для сохранения, названия ОП, наследует функция save_op
#button_save = Button(underline=0,text='Сохранить название операционной системы.',command=save_op);button_save.place(x=1,y=90)
#
#
#
## Создание вечного цикла, для работы приложения
#windows.mainloop()

a = "5555"
a = float(a)
print(a)
print(type(a))