import datetime
import time

while True:
    time.sleep(60)
    start = open('startsleep.txt','r')
    start_sleep = start.read()

    a= str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute)
    a = list(a)


