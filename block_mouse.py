#import pynput
#while True:
  #  mouse_listen = pynput.mouse.Listener(suppress=True)
    #mouse_listen.start()


import pyautogui
import keyboard
pyautogui.FAILSAFE = False
while True:
    for x in range(955,960):
        for y in range(534,540):
            pyautogui.moveTo(x,y)
