import os
host_path =r'C:\Windows\System32\drivers\etc\hosts'

website_list = [input('Введите URL сайта, дабы его заблокировать.').replace('https://','').replace('/','')]
redirect = '127.0.0.1'
file = open(host_path,'r+')
content = file.read()
print(content)
for website in website_list:
    if website in content:
        pass
    else:
        file.write(redirect + " " + website + "\n")



