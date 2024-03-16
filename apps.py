from tkinter import *
import os






def save_token():
    global con4
    token = con4.get()
    if len(token)==0:
        war = Label(text = 'Ошибка введите токен.').place(x=15,y=385)
    else:
        try:
            f = open('token.txt','w')
            f.truncate(0)
            f.write(token)
            f.close()
            ff = open('token_status.txt','w')
            ff.truncate(0)
            ff.write('1')
            ff.close()
            con6 = Label(text='ВНИМАНИЕ!').place(x=0, y=390)
            con7 = Label(text='Теперь чтобы использовать бота перейдите по ссылке (самая первая, которая начинается на "t.me") и перезагрузите компьютер.').place(x=0,y=410)
            con8 = Label(text = 'Перезагрузить компьютер?').place(x=0,y=430)
            def rest():

                os.system("shutdown /r /t 1")

            def poki():
                os.system(f"taskkill /f /im apps.exe")

            but_yes_rest = Button(text = 'Да.',width=8,command=rest).place(x=0,y=455)
            but_no_rest = Button(text='Нет.',width=8,command=poki).place(x=70,y=455)

        except:
            war = Label(text='Ошибка введите токен.').place(x=15, y=385)





window = Tk()
window.title("Настройка и подключение бота.")
window.geometry("850x550")
window.resizable(False,False)
window.iconphoto(False, PhotoImage(file='Settings.ico'))


image = PhotoImage(file="BotFather.png")
lab_oq = Label(text='OR-код на BotFather:').place(x=444,y=0)
label = Label(image=image).place(x=444,y=20)

photo_token = PhotoImage(file="SeeToken.png")
photo_see_token = Label(text='Вид токена(пример):').place(x=490,y=260)
lb = Label(image=photo_token).place(x=490,y=280)



lab = Label(text = 'Начнём настройку:').place(x=0,y=0)
lab1 = Label(text = '1) Откройте приложение "Telegram" на ПК или смартфоне.').place(x=5,y=20)
lab2 = Label(text = '2) В поиске наберите "@BotFather" и создайте чат.').place(x=5,y=40)
lab3 = Label(text = '3) В открывшемся чате введите команду "/newbot" ').place(x=5,y=60)
lab4 = Label(text = '4) Далее введите название вашего бота. Оно может быть любое.').place(x=5,y=80)
lab5 = Label(text = '5) Теперь давайте придумем username бота.').place(x=5,y=100)
lab6 = Label(text = 'Примечание: username должен оканчиваться на "bot"').place(x=10,y=120)
lab7 = Label(text = '6) Отлично вы успешно создали бота!').place(x=5,y=140)


con = Label(text = 'Подключение бота:').place(x=0,y=250)
con1 = Label(text = '1) Сгенирированный токен (тёмно-синий текст, чёрный на смартфоне) скопируйте.');con1.place(x=10,y=270)
con2 = Label(text = '2) Вставьте скопированный текст ниже и переключитесь на "en" раскладку.');con2.place(x=10,y=290)
con3 = Label(text = '3) И нажмите кнопку "Сохранить токен". И следуйте дальнейшим инструкциям.');con3.place(x=10,y=310)
con4 = Entry(width=50);con4.place(x=15,y=335)

but = Button(text = 'Сохранить токен.',command=save_token);but.place(x=15,y=360)








window.mainloop()
