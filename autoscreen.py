#import time
import pyautogui
import  datetime
#
#
#while True:
#    date = datetime.datetime.today()
#    timing = date.strftime('%H:%M:%S')
#    timing = str(timing)
#    time.sleep(5)
#    screen = pyautogui.screenshot('screen' + timing + '.png')

import time
import screen
import random


while True:
    file = open('timeauto.txt', 'r')
    timing = int(file.read())
    time.sleep(timing)
    file.close()
    date = datetime.datetime.today()
    tim = date.strftime('%H:%M:%S')
    tim = str(tim)
    tim = tim.replace(':','.')
    screen = pyautogui.screenshot(f'savescreen/{tim}.png')








