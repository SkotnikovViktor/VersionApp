# Импорт библиотек для работы самого кода
# Импорт tkinter для создание интерфейса приложения
from tkinter import *
# Импорт библиотеки для загрузки файлов
import wget
# Создание переменных
check_watch_button = 0

# Создание окна:
# Создаём переменную windows и присваиваем ей метод по созданию окна Tk()
windows = Tk()
# Стави флашки на запрет, измменения геометри окна
windows.resizable(width=False,height=False)
# Указываем размеры окна по x и y
windows.geometry('680x500')
# Даём название нашему окну и всему главному приложению
windows.title('Настройки')


# Здесь создаётся функция по сохранению информации об операционной системы пользователя
### Начало функции
def save_op():
    # Объявляем глобальную переменную name_op
    global name_op,check_watch_button
    # Создана переменная name_op для того, чтобы принять информацию об введёном ОП пользователя
    name_op = input_name_op.get()
    if len(name_op)==0:
           label_save= Label(text='Введите название ОП!',fg = 'red');label_save.place(x=325,y=62)
    else:
        if check_watch_button==1:
                label_save= Label(text='Изменения сохранены!',fg = 'green');label_save.place(x=325,y=62)
                # Создаём кнопку для установки программы для введёной ОП, а также проверяем отступ
                button_install_program = Button(text=f'Установить программу для: {name_op}',underline=0);button_install_program.place(x=400-len(name_op)*3,y=465)
                # Сохраняем эту информацию в файл с флагом "w" если файл нету, то создаётся новый, а если есть то файл перезаписываеться
                file_op = open('information_op.txt','w')
                # Записываем эту информацию в файл, и убираем все пробелы методом replace
                file_op.write(name_op.replace(' ',''))       
        else:
            label_save = Label(text='Сохранено!',fg='green');label_save.place(x=325,y=62)
            # Создаём кнопку для установки программы для введёной ОП, а также проверяем отступ
            button_install_program = Button(text=f'Установить программу для: {name_op}',underline=0);button_install_program.place(x=400-len(name_op)*3,y=465)
            # Сохраняем эту информацию в файл с флагом "w" если файл нету, то создаётся новый, а если есть то файл перезаписываеться
            file_op = open('information_op.txt','w')
            # Записываем эту информацию в файл, и убираем все пробелы методом replace
            file_op.write(name_op.replace(' ',''))
    check_watch_button = 1
    return name_op
    #### Конец функции





# Создаём текстовое поле, с текстом "Напишите полное название вашей ОП"
text_PO = Label(text='Напишите полное название вашей операционной системы:',font='Ubuntu',underline=0);text_PO.place(x=1,y=0)
# Создаём текстовое поле, с примеро ввода текста
text_PO_primer = Label(text='Например: Linux, Windows 7-11.',font='Ubuntu',underline=10);text_PO_primer.place(x=1,y=35)
# Создаем поле для ввода текста с название ОП
input_name_op = Entry(text = 'Введите название ПО:',font='Ubuntu',foreground='black',width=35);input_name_op.place(x=1,y=60)
# Создаем кнопку для сохранения, названия ОП, наследует функция save_op
button_save = Button(underline=0,text='Сохранить название операционной системы.',command=save_op);button_save.place(x=1,y=90)



##### Тестовая ветка(пока в разработке)
# Создаём текстовое поле с тектом "Установка зависимых пакетов:"
text_install_package = Label(text='Установка зависимых пакетов:',font='Ubuntu',underline=0);text_install_package.place(x=1,y=160)
# Создание кнопки для установки зависимых пактов: шрифтов и так далее...
button_install_package = Button(underline=0,text='Установить зависимые пакеты.');button_install_package.place(x=1,y=190)
##### Тестовая ветка(пока в разработке)


# Создание вечного цикла, для работы приложения
windows.mainloop()