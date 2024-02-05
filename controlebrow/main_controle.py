import os
def add_site():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    website_list = input('Введите URL сайта, дабы его заблокировать----> ').replace('https://','')
    if website_list[-1]=='/':
        website_list = website_list[:-1]
        print(website_list)
    website_list=[website_list]
    redirect = '127.0.0.1'
    file = open(host_path,'r+')
    content = file.read()
    print(content)
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")
            print('Выполнено успешно! Требуется перезагрузка!')
            res = input(
                'Выполниить перезагрузку(Yes\Да) или (No\Нет), если вы хотите добавить ещё сайт то введите команду "Добавить":')
            res = res.replace(' ', '')
            if res == "Да" or res == "Yes":
                os.system("shutdown /r /t 1")
            elif res == "Нет" or res == "No":
                print("Закрытие прграммы.")
            elif res == 'Добавить':
                add_site()
add_site()




