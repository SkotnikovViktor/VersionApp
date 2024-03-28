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
    print(today)
    time.sleep(1)
    today = int(today)
    today = today//60//60
    today = round(today)
    print(today)

    if todayday == 0:
        mon = open('monday.txt','r+')
        mon.truncate(0)
        mon.write(str(today))
        mon.close()
    elif todayday == 1:
        tue = open('tuesday.txt','r+')
        tue.truncate(0)
        tue.write(str(today))
        tue.close()

    elif todayday == 2:
        wed = open('wednesday.txt','r+')
        wed.truncate(0)
        wed.write(str(today))
        wed.close()

    elif todayday==3:
        thu = open('thursday.txt','r+')
        thu.truncate(0)
        thu.write(str(today))
        thu.close()

    elif todayday == 4:
        fri = open('friday.txt','r+')
        fri.truncate(0)
        fri.write(str(today))
        fri.close()

    elif todayday==5:
        sat = open('saturday.txt','r+')
        sat.truncate(0)
        sat.write(str(today))
        sat.close()

    elif todayday == 6:
        sun = open('sunday.txt','r+')
        sun.truncate(0)
        sun.write(str(today))
        sun.close()








