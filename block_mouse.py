#import pynput
#while True:
 #   mouse_listen = pynput.mouse.Listener(suppress=True)
  #  mouse_listen.start()


import pyautogui
pyautogui.FAILSAFE = False
while True:
    pyautogui.moveTo(0,0)
