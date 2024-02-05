import time
from ctypes import *
import os
import pynput
def block_klav():
    while True:
        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        mouse_listener = pynput.mouse.Listener(suppress=True)
        # Метод start запускает выше стоящие функции, клавиатура и мышка блокируются, есть команда stop()
        keyboard_listener.start()
        mouse_listener.start()


file = open('check.txt','w')
file_check = file.write('1')
file.close()
time_off = 15
while time_off>0:
    time_off-=1
    time.sleep(1)
    print(time_off)
    if time_off==0.0 or round(time_off)==0:
        block_klav()







