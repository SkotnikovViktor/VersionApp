from datetime import *
import time
from uptime import *



k = 0

datetime.today()
## Узнаём день недели
todayday = datetime.today().weekday()


## 0 - понедельник
# 1 - вторник
# 2 - среда
# 3 - четверг
# 4 - пятница
# 5 - суббота
# 6 - воскресенье

while True:
    today = uptime()
    time.sleep(1)
    today = int(today)
    print(today)
    print(type(today))
    if todayday == 0:
        mon = open('monday.txt','r+')
        mon.write(str(today))
        mon.close()
    elif todayday == 1:
        tue = open('tuesday.txt','r+')
        tue.write(str(today))
        tue.close()
    elif todayday == 2:
        wed = open('wednesday.txt','r+')
        wed.write(str(today))
        wed.close()
    elif todayday==3:
        thu = open('thursday.txt','r+')
        thu.write(str(today))
        thu.close()
    elif todayday == 4:
        fri = open('friday.txt','r+')
        fri.write(str(today))
        fri.close()
    elif todayday==5:
        sat = open('saturday.txt','r+')
        sat.write(str(today))
        sat.close()
    elif todayday == 6:
        sun = open('sunday.txt','r+')
        sun.write(str(today))
        sun.close()








