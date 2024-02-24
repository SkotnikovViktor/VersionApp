import time
from datetime import *
import time

k = 0



datetime.today()
todayday = datetime.today().weekday()
print(type(todayday))

# 0 - понедельник
# 1 - вторник
# 2 - среда
# 3 - четверг
# 4 - пятница
# 5 - суббота
# 6 - воскресенье

while True:
    k+=1
    print(k)
    time.sleep(0.9)
    if todayday == 0:
        mon = open('monday.txt','w')
        mon.write(str(k))
    elif todayday == 1:
        tue = open('tuesday.txt','w')
        tue.write(str(k))
    elif todayday == 2:
        wed = open('wednesday.txt','w')
        wed.write(str(k))
    elif todayday==3:
        thu = open('thursday.txt','w')
        thu.write(str(k))
    elif todayday == 4:
        fri = open('friday.txt','w')
        fri.write(str(k))

    elif todayday==5:
        thu = open('thursday .txt','w')
        thu.write(str(k))
    elif todayday == 6:
        sun = open('sunday.txt','w')
        sun.write(str(k))






