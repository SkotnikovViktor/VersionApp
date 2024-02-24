import os
def del_lis_site():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    website_list = open('site_unblock.txt','r')
    website_list = str(website_list.read().replace('https://',''))
    print(website_list)
    if website_list[-1]=='/':
        website_list = website_list[:-1]
        print(website_list)
    website_list = [website_list]
    file = open(host_path, 'r+')
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
        file.truncate()
del_lis_site()
os.system("shutdown /r /t 1")
