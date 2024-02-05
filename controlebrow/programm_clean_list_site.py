import os
def del_lis_site():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    website_list = input('Введите URL сайта, дабы его разблокировать---->  ').replace('https://','')
    if website_list[-1]=='/':
        website_list = website_list[:-1]
    website_list = [website_list]
    file = open(host_path, 'r+')
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()
    print('Выполнено успешно! Требуется перезагрузка!')
    res = input(
        'Выполниить перезагрузку(Yes\Да) или (No\Нет), если вы хотите удалить ещё сайт то введите команду "Удалить":')
    res = res.replace(' ', '')
    if res == "Да" or res == "Yes":
        os.system("shutdown /r /t 1")
    elif res == "Нет" or res == "No":
        print("Закрытие прграммы.")
    elif res == 'Удалить':
        del_lis_site()
del_lis_site()
