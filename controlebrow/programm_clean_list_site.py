def del_lis_site():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    website_list = [input('Введите URL сайта, дабы его разблокировать.').replace('https://','').replace('/','')]
    file = open(host_path, 'r+')
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()
del_lis_site()