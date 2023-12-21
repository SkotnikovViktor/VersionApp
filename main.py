from tkinter import *
import wget
windows = Tk()
#a=BooleanVar()
#checkbut_linux = Radiobutton(text='Дистрибутив Linux',variable=a,value=False);checkbut_linux.place(x=0,y=20)
#checkbut_windows = Radiobutton(text='Windows 7-11',variable=a,value=True);checkbut_windows.place(x=0,y=40)

def save_op():
    global name_op
    name_op = input_name_op.get()
    s = len(name_op)*3
    button_install_program = Button(text=f'Установить программу для: {name_op}');button_install_program.place(x=400-s,y=465)

    
text_PO = Label(text='Напишите полное название вашей операционной системы:');text_PO.place(x=0,y=0)
input_name_op = Entry(text = 'Введите название ПО:');input_name_op.place(x=2,y=30)
button_save = Button(text='Сохранить название операционной системы.',command=save_op);button_save.place(x=0,y=55);save_op()





windows.geometry('680x500')
windows.title('Настройка главной программы')
windows.mainloop()