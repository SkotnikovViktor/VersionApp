import psutil
s = []
processes = psutil.process_iter()
for process in processes:
    if process.name() != 'svchost.exe' and process.name() != 'System Idle Process' and process.name()!='System' and process.name()!='Registry':
        s.append(process.name())
        file = open('process.txt','w')
        a = '\n'.join(s)
        file.write(a)
        file.close()
