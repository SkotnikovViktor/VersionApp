#import time
#import pyautogui
#import  datetime
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
    file.close()
    time.sleep(timing)
    k = random.randint(111111111, 999999999)
    screen.doingscreen(f'savescreen/{k}.png')








