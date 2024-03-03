import os
import time
import psutil


while True:
    time.sleep(20)
    s = []
    processes = psutil.process_iter()
    for process in processes:
        if process.name() != 'svchost.exe' and process.name() != 'System Idle Process' and process.name()!='System' and process.name()!='Registry':
            s.append(process.name())




    if 'main.exe' not in s:
        #print('0')
        try:
            os.startfile('main.exe')
        except:
            pass
    else:
        pass


    if 'writing_time_screen.exe' not in s:
        try:
            os.startfile('writing_time_screen.exe')
        except:
            pass
    else:
        pass




